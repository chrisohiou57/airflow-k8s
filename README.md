# airflow-k8s

**NOTE after pulling the actual password needs to be replaced in git-sync-secret.yaml for git-sync sidecar to work.**

##### I believe this is the official Airflow Helm chart
https://github.com/airflow-helm/charts/tree/main/charts/airflow
##### Seems to be an overview of all possible values for the Helm chart
https://github.com/airflow-helm/charts/blob/airflow-8.0.1/charts/airflow/values.yaml#L270-L276

```
export RELEASE_NAME=airflow-cluster
export NAMESPACE=airflow
export CHART_VERSION=8.0.8
export VALUES_FILE=./helm/kubernetes-executor-values.yaml
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
