Assignment: Prompting, Debugging, and Innovation for Code Generation with LLMs

Overview:-
This project evaluates and improves the performance of two large language model (LLM) families — DeepSeek 1.3B (a Hugging Face Transformer) and LLaMA 3 — on code generation tasks. Both models were downloaded and run locally to avoid API dependencies.
The experiments focus on generating, testing, and refining Python programs using various prompting strategies, including Chain-of-Thought (CoT), Self-Debugging, and a novel strategy (CGCS) proposed in this project.

Dataset:-
The HumanEval dataset was used for evaluation.
Ten problems were selected and stored in new_data.json (available in the dataset/ folder).

Prompting Strategies Used:-
 1.Chain-of-Thought (CoT) Prompting
 2.Self-Debugging Prompting

Constraint-Guided Code Synthesis (CGCS) – Novel strategy proposed in this project

Experiment Workflow:-

  1. Initial Code Generation
      Scripts used:
      generate_deepseek_initial.py and 
      generate_llama_initial.py

      Output location:
      Generated code files saved in outputs/

  2. Initial Testing
      Scripts used:
      initial_deepseek_test.py and 
      initial_llama_test.py

     Evaluation metric: pass@1
     Results stored in the results/ folder.

  3.Targeted Refinement
    Two common problems failed across both LLM families and both prompting strategies (CoT and Self-Debugging):
    is_balanced_parentheses
    matrix_rotate_9
    
    To address these, their prompts were enhanced in refined_prompt_dataset.json.
    Regeneration scripts:
    generate_llama_refined.py
    generate_deepseek_refined.py
    Output: refined_outputs/
    
    Testing scripts:
    refined_deepseek_test.py
    refined_llama_test.py
    Results (stored in results/) showed that both targeted problems passed all test cases, improving the overall pass@1 accuracy.

  4.Novel Strategy: CGCS (Constraint-Guided Code Synthesis)
   After the refinement, a new strategy — CGCS — was developed and tested across both LLM families.

   Workflow:-

   Modified all 10 problem prompts following CGCS logic and saved them in cgcs_data_prompt.json.

   Code generation scripts:
   cgcs_deepseek_generate.py
   cgcs_llama_generate.py

   Testing scripts:
   cgcs_test_deepseek.py
   cgcs_test_llama.py

   Evaluation metric: pass@1
   All generated codes are stored in deepseek_cgcs_outputs and llama_cgcs_outputs folder. Test results are stored in the  results/ folders respectively.
