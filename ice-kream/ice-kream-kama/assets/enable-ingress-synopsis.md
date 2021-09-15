# Enabling Ingress

## What does it Mean?

By default the Ice Kream store is not available on the world 
wide web. If you want to make it available on a specific domain,
e.g **[ice-kream.nmachine.io](https://ice-kream.nmachine.io)**. To do this,
we need to use Kubernetes' 
**[Ingress](/)** and 
**[Certificate Manager](/)** resources. This operation takes you
through the setup.

## Requirements

You will need the following:
- An **[Ingress Controller](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/)** present in the cluster.
- A **[`cert-manager`](https://cert-manager.io/docs/)** present in the cluster.
- A **domain name** that you can configure.

## Getting an Ingress Controller

An **[Ingress Controller](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/)**
is a Kubernetes resource that handles routing traffic. As per the guide linked here,
there is a variety of options to choose from. We recommend using an Nginx controller,
which you can get in one of three ways:
- The official **[Nginx NMachine](/)** for guaranteed compatibility **(Recommended)**
- The **[Helm chart](/)**
- The **[raw manifest](/)**

## Getting a `cert-manager`

A **[Certificate Manager](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/)**
is a Kubernetes resource that handles routing traffic. As per the guide linked here,
there is a variety of options to choose from. We recommend using an Nginx controller,
which you can get in one of three ways:
- The official **[Cert-man NMachine](/)** for guaranteed compatibility **(Recommended)**
- The **[Helm chart](https://cert-manager.io/docs/installation/helm)**
- The **[raw manifest](https://cert-manager.io/docs/installation/)**
