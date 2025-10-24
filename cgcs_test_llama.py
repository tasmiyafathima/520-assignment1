# final_llama_test.py
import os
import json

# =====================
# CONFIG
# =====================
DATASET_FILE = "cgcs_data_prompt.json"  # same JSON file used for generation
FOLDERS = {
    "CGCS": "llama_cgcs_outputs"
}

# =====================
# UTILITY FUNCTION
# =====================
def run_tests(code: str, tests: str) -> bool:
    """
    Run the generated code against its test cases.
    Returns True if all tests pass.
    """
    try:
        local_vars = {}
        exec(code, local_vars)     # define functions
        exec(tests, local_vars)    # run assertions
        return True
    except Exception:
        return False

# =====================
# EVALUATE FUNCTION
# =====================
def evaluate_folder(folder_path: str, problems: list, output_json: str):
    results = {}
    total = 0
    passed = 0

    print(f"\nEvaluating generated code in {folder_path} ...\n")

    for prob in problems[:10]:  # only first 10 problems
        pid = prob.get("id", f"prob_{problems.index(prob)}")  # fixed typo
        code_file = os.path.join(folder_path, f"{pid}.py")
        tests = prob["tests"]

        if not os.path.exists(code_file):
            print(f"[!] Missing generated file for {pid}")
            results[pid] = {"passed": False, "file": code_file}
            continue

        with open(code_file) as f:
            code = f.read()

        ok = run_tests(code, tests)
        results[pid] = {"passed": ok, "file": code_file}

        total += 1
        passed += int(ok)
        print(f"[{'PASS' if ok else 'FAIL'}] {pid}")

    pass_at_1 = passed / total * 100 if total else 0
    print(f"\n=== PASS@1: {pass_at_1:.2f}% ({passed}/{total}) ===")

    with open(output_json, "w") as f:
        json.dump({"pass@1": pass_at_1, "details": results}, f, indent=2)

    print(f"Results saved to {output_json}")


# =====================
# MAIN
# =====================
def main():
    # load problem dataset
    with open(DATASET_FILE) as f:
        problems = json.load(f)

    # evaluate both folders
    for strategy, folder in FOLDERS.items():
        output_json = f"cgcs_results_pass1_llma_{strategy}.json"
        evaluate_folder(folder, problems, output_json)


if __name__ == "__main__":
    main()
