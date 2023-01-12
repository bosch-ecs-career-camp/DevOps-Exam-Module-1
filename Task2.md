# Pipeline

> Please continue with this current task only after [task1](./Task1.md) is finished.

## As a bosch ultimate goal, we are aiming to improve our customer products. Thats why we want to improve the program delivery to our client from the Carshop.
### Based on the program created in [task1](./Task1.md) we can now think for creation of a CI solution with Github Workflows.

1. Our furthure task is to create a pipeline with the name "Execution" which is running only on a Pull Request.
2. The Pipeline can work on both Linux & Windows, the chose is yours.
3. After that the pipeline should be created in a sequence of 4 consequitive jobs each one starting only after the previous job execution is done.

- Job1: [Checkout]
- Job2: [Run Python Execution]
- Job3: [Archive Python Artifacts]
- Job4: [Development Information]

Pipeline/Git
 - return github key->values with restapi:
	"actor",
	"triggering_actor",
	"triggering_actor"->"action",
	"head_ref",
	"os",
	"arch",
	"workspace"
