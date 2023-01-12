# Task2 - GitHub Workflow design and implementation

> Please continue with this current task only after [task1](./Task1.md) is finished.

Our ultimate goal in Bosch is that we are aiming to improve our customer products. Thats why we want to improve the program delivery to our client from the Carshop.
Based on the program created in [task1](./Task1.md) we can now think for creation of a CI solution with Github Workflows.

1. Our furthure task is to create a pipeline with the name "Profit Execution" which is running only on a push events.
2. There should be a manual choice input where you can specify for which month from task1 you can see the profit.( The default value should be "3" - month(March).
3. Only one pipeline of the same type should run at once.
4. The Pipeline should run under Linux OS.
5. After that the pipeline should be created in a sequence of 4 consequitive jobs each one starting only after the previous job execution is done.

- Job1: [Checkout]
- Job2: [Run Python Execution]
- Job3: [Archive Python Artifacts]
- Job4: [Development Information]


# Detailed Requirement of each job:

- Job1: [Checkout]
	* Checkout the python script folder developed in task1.
- Job2: [Run Python Execution]
	* Execute the python script developed in task1 by providing the manual choice input created earlier as an argument to the python script.
- Job3: [Archive Python Artifacts]
	* Archive the outputed file Generated in Job2 after a successful execution of the python program. ("profit.txt")
- Job4: [Development Information]
 	* Display the following information for the current running workflow directly in the console or in a file named log_file.log created in the default workspace.
	- "actor",
	- "triggering_actor",
	- "head_ref",
	- "os",
	- "arch",
	- "workspace"
