---
Category: note
Date: '2022-05-12'
Modified: '2023-07-12'
Slug: auto-documented-makefile
Status: published
Tags: auto-documented, makefile, documentation, help, make-help
Title: Auto Documented Makefile
---
X::[[make]]

When working on large projects, it can be challenging to keep track of all the different make targets and their purposes. Fortunately, there's a solution to this problem: an auto-documented makefile. With this approach, you can add help information to your makefile, which will be automatically generated based on the comments in your code. This way, you can quickly and easily see what each target does, without having to go through the entire makefile to find the relevant information.

The code provided in the example below is an example of how to add an auto-documented help option to make. The key part of the code is the `help` target, which is a `PHONY` target, meaning it's not associated with a file. The target uses `sed` to extract the comments that start with "##" and save them in a hold space. These comments are then printed and sorted in alphabetical order.

The following is the key part of the code:
```
.PHONY: help
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \

```

This `sed` script is used to extract the comments that start with "##" and save them in a hold space. Each option should have a comment above, as in the example:

```
## Convert markdown to pdf
pdf:	
	pandoc -N --toc --template template.latex --filter pandoc-citeproc -o README.pdf README.md
```

Then, the script uses `awk` to format the output and `more` to display the help information. The script uses the `MAKEFILE_LIST` variable, which contains the names of all the makefiles that are included by make.

To use this code, you should add the code snippet at the end of your makefile and make sure that your makefile follows the pattern where each option should have a comment above, as in the example above.

With this code in place, you can simply run `make help` in your terminal, and you'll see a list of all the available make targets, along with their associated help information. This can save you a lot of time and make it much easier to navigate your makefile, even on large projects.


## Original makefile

Code at the end of Makefile.
```
# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: help
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
```


**Credits:**

Code was found in some project, original author of the code unknown.
http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html