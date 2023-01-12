# Task2 - Pipeline

> Please continue with this current task only after [task1](./Task1.md) is finished.

As a bosch ultimate goal, we are aiming to improve our customer products. Thats why we want to improve the program delivery to our client from the Carshop.
Based on the program created in [task1](./Task1.md) we can now think for creation of a CI solution with Github Workflows.

1. Our furthure task is to create a pipeline with the name "Execution" which is running only on a Pull Request.
2. The Pipeline can work on both Linux & Windows, the choise is completely yours.
3. After that the pipeline should be created in a sequence of 4 consequitive jobs each one starting only after the previous job execution is done.

- Job1: [Checkout]
- Job2: [Run Python Execution]
- Job3: [Archive Python Artifacts]
- Job4: [Development Information]


# Detailed Requirement of each job:

- Job1: [Checkout]
	* Checkout the python script folder developed in task1.
- Job2: [Run Python Execution]
	* Execute the python script developed in task1 and save the output to a file.
- Job3: [Archive Python Artifacts]
- 	* Archive the file Generated in Job2
- Job4: [Development Information]
 	* Display the following information for the current running workflow directly in the logs.
		"actor",
		"triggering_actor",
		"head_ref",
		"os",
		"arch",
		"workspace"
