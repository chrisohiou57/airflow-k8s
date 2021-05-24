# airflow-k8s

##### I believe this is the official Airflow Helm chart
https://github.com/airflow-helm/charts/tree/main/charts/airflow
##### Seems to be an overview of all possible values for the Helm chart
https://github.com/airflow-helm/charts/blob/airflow-8.0.1/charts/airflow/values.yaml#L270-L276

## Installation - Minikube
After cloning the repository and navigating to the base directory of the repo set the following environment variables:
```
export RELEASE_NAME=airflow-cluster
export NAMESPACE=airflow
export CHART_VERSION=8.0.8
export VALUES_FILE=./helm/kubernetes-executor-values.yaml
```

You will need to create the K8s Namespace and Secret that contains GitHub credentials prior to installing the Helm chart. You can do that by running:
```
kubectl apply -f helm/namespace.yaml
kubectl apply -f helm/git-sync-secret.yaml
```

##### Install the chart (Helm 3)
```helm install $RELEASE_NAME airflow-stable/airflow --namespace $NAMESPACE --version $CHART_VERSION --values $VALUES_FILE```

##### Verify the installation
```helm list -n $NAMESPACE```

##### Expose the web app with port forwarding
```
export POD_NAME=$(kubectl get pods --namespace $NAMESPACE -l "component=web,app=airflow" -o jsonpath="{.items[0].metadata.name}")
kubectl port-forward --namespace $NAMESPACE $POD_NAME 8080:8080
```

##### If running in minikube, you can see how to access the app by running:
```minikube service --url airflow-cluster-web -n airflow```

##### Uninstall the chart (Helm 3)
```helm uninstall $RELEASE_NAME -n $NAMESPACE```

##### Delete the namespace
```kubectl delete namespace airflow```