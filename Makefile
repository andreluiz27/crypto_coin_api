# Makefile for Python project with Docker Compose

# Variables
DOCKER_COMPOSE = docker-compose
PYTHON = python3

# Default target
.PHONY: help
help:
	@echo "Makefile commands:"


# Start services
.PHONY: api
api:
	$(DOCKER_COMPOSE) up -d --build
