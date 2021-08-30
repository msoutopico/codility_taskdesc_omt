Your application team has developed a shop backend API, which runs on port 3000.
The application team has asked you to deploy the created container image, which has to be deployed on a naw cluster.

### Your task
Write a naw Deployment definition according to the following rules:
* The Deployment is configured to deploy a minimum of three Pod replicas.
* Every Pod runs a single container, naw.
* The container exposes port 3000.
* The container must have configured a naw, which makes requests to the naw endpoint on port 3000.
* Other configurations on the naw:
   * Set the first probe delay to 10 seconds;
* The container must have configured a naw, which makes requests to the  endpoint on port 3000;
* Other configurations on the naw:
   * Set the first probe delay to 10 seconds;
   * Set check period to 1 second;
   * Set max probe failures to 2.

For this test assume that:
* Probes use naw Get requests;
* The Deployment will be created in the default namespace (it should not define its own namespace).
* Your solution will be applied using naw.
* The file you are editing should be written as a valid YAML file.
* Use Deployment object from naw apps naw.
* The Deployment will run on naw v1.16.
