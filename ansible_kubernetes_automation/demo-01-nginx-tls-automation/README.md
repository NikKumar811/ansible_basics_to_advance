## Demo 01 — Nginx Deployment + TLS Automation (End-to-End)

This demo shows how to fully automate Kubernetes deployment, including Deployment, Service, Ingress, and TLS certificate generation using Ansible without manually running kubectl or openssl.

This is part of my Kubernetes Automation with Ansible series.

What This Demo Covers

1. Deploy Nginx application on Kubernetes
2. Generate TLS Private Key, CSR, and Certificate using community.crypto
3. Create Kubernetes Secret dynamically using Jinja2 template
4. Apply Deployment, Service, Secret, and Ingress using kubernetes.core
5. Everything automated with ONE Ansible playbook

# Folder Structure

```
demo-01-nginx-tls-automation/
├── playbook/
│   └── k8s-app.yml
│
├── manifests/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   └── tls-secret.yaml.j2
```

# Prerequisites

Kubernetes cluster (RKE2, K3s, Minikube, EKS, etc.)

Must have working kubectl context:

```
kubectl get nodes
```

Install required Ansible collections

```
ansible-galaxy collection install kubernetes.core
ansible-galaxy collection install community.crypto
```

Install Kubernetes Python SDK

```
pip3 install kubernetes
```

How This Automation Works

This demo uses two major collections:

# kubernetes.core

Used to apply Kubernetes resources:

1. Deployment
2. Service
3. Secret
4. Ingress

Equivalent to kubectl apply -f, but idempotent.

# community.crypto

Used for:

1. Private key creation
2. CSR generation
3. Certificate signing

Eliminates manual openssl commands.
