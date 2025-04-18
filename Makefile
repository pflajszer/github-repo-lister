MOUNT_DIRECTORY=directory_path_where_you_want_your_output_file
build:
	docker build -f deployment/Dockerfile -t pflajszer/github-repo-lister .
run:
	docker run -v "${MOUNT_DIRECTORY}:/app/output" pflajszer/github-repo-lister