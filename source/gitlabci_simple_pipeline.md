**Note: This task verifies knowledge of GitLab CI configuration skills based on simplified use case scenarios. Each command added to the YAML should be a one-liner without extra bash functions.**

Your development team is building a new e-Commerce application. The implementation phase has been finished and your role is to build a GitLab CI pipeline for testing that application.

You have been provided with a Docker image with tests implemented in Java. The Docker image is named `java-tests-repository` and is accessible via Docker Hub with a tag, `latest`. Use it to build a pipeline with two defined stages: `compile` and `test`.

Define a `build` job for the `compile` stage, which should compile the provided Java classes with the following command:

```javac -d /src/tests/suites/ -cp /lib/junit-4.12.jar /data/sets/users.java```

For the `test` stage there should be three jobs called `registration`, `payments` and `orders`, which will start various testing suites. Be sure to run them **in parallel**. Each of them should execute a Maven script to start the tests.

Example Maven script for `registration` and `orders` is:

```mvn clean test -Dtest=functional -Ddata_sets=users```,

while for `payments` it's:

```mvn clean test -Dtest=performance -Ddata_sets=users```.

For the rest of the jobs you should use complementary commands, replacing the `-Dtest` parameter's value with the name of the job.

Use a `default` section to define globally a script which will be executed before all jobs. It should execute a command to install Maven: `mvn install`.
