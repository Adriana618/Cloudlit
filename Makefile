DEVTAG = dev-$$USER
REPOSITORY = alonso139

.PHONY: deploy
deploy: build-api-image upload-api-image
	-kubectl apply -f kubernetes/cloudlit-services.yaml
	-kubectl apply -f kubernetes/cloudlit-configmap.yaml
	-kubectl apply -f kubernetes/cloudlit-deploy.yaml
	-kubectl apply -f kubernetes/cloudlit-autoscaling.yaml
	-kubectl set image deployment/cloudlit-django-api cloudlit-django-api=$(REPOSITORY)/cloudlit-django-api:$(DEVTAG)

.PHONY: rebuild-api
rebuild-api: build-api-image upload-api-image
	-kubectl apply -f kubernetes/cloudlit-autoscaling.yaml
	-kubectl apply -f kubernetes/cloudlit-configmap.yaml
	-kubectl rollout restart deployment cloudlit-django-api
	-kubectl set image deployment/cloudlit-django-api cloudlit-django-api=$(REPOSITORY)/cloudlit-django-api:$(DEVTAG)

.PHONY: upload-api-image
upload-api-image: login-docker
	-docker tag cloudlit-django-api:$(DEVTAG) $(REPOSITORY)/cloudlit-django-api:$(DEVTAG)
	-docker push $(REPOSITORY)/cloudlit-django-api:$(DEVTAG)

.PHONY: login-docker
login-docker:
	-docker login --username alonso139 --password Comofunciona1

.PHONY: build-api-image
build-api-image:
	-docker build . --file docker-conf/Dockerfile-django-api --tag cloudlit-django-api:$(DEVTAG)