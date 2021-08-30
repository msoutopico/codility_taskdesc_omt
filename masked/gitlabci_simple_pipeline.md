Note: This task checks knowledge of naw CI configuration skills based on simple use cases. Each command added to the YAML should be a one-liner without extra naw functions.

Your development team is building a new e-Commerce application. The creation phase has been finished and your role is to build a naw CI pipeline for testing that application.

You have been given a Docker image with tests done in Java. The Docker image is named java tests repository and is accessible through Docker Hub with a tag, latest. Use it to build a pipeline with two defined stages: compile and test.

Define a build job for the compile stage. This should compile the Java classes with the following command:

naw