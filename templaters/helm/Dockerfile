FROM python:3.6

RUN apt-get update && apt-get install git \
                                      curl

ADD requirements.txt .
RUN pip3 install -r requirements.txt

RUN curl https://get.helm.sh/helm-v3.1.0-linux-amd64.tar.gz --output helm_bin.tar.gz
RUN tar -zxvf helm_bin.tar.gz
RUN mv linux-amd64/helm /usr/local/bin
RUN rm helm_bin.tar.gz
RUN rm -rf linux-amd64

ADD . /nectar

#RUN helm repo add stable https://kubernetes-charts.storage.googleapis.com/
#RUN helm repo update

#ENTRYPOINT ["python", "nectar/main.py"]