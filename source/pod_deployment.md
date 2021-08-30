Your application team has developed a shop backend API, which runs on port `3000`.
The application team has asked you to deploy the created container image, which has to be deployed on a Kubernetes cluster.

### Your task
Write a Kubernetes Deployment definition according to the expectations listed below:
* The Deployment is configured to deploy a minimum of `three` Pod replicas;
* Every Pod runs a single container, `hub.example.com/shop-backend:1.0.0`;
* The container exposes port `3000`;
* The container must have configured a LivenessProbe, which makes requests to the `/healthz` endpoint on port `3000`;
* Additional configurations on the LivenessProbe:
    * Set initial probe delay to `10 seconds`;
* The container must have configured a ReadinessProbe, which makes requests to the `/` endpoint on port `3000`;
* Additional configurations on the ReadinessProbe:
    * Set initial probe delay to `10` seconds;
    * Set check period to `1` second;
    * Set max probe failures to `2`.

For this test assume that:
* Probes use `httpGet` requests;
* The Deployment will be created in the `default` namespace (it is not expected to define its own namespace);
* Your solution will be applied using `kubectl apply -n default -f solution.yaml`;
* The file you are editing should be written as a valid YAML file;
* Use Deployment object from apiGroup `apps/v1`;
* The Deployment will run on Kubernetes v1.16.
