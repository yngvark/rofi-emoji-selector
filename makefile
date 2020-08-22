.PHONY: help
help: ## print this menu
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

run: ## Run rofi with emoji mode only
	rofi -show emoji -modi emoji:./emoji-selector.py

combi: ## Run rofi in combi mode
	rofi -modi combi -combi-modi "run,window,emoji:./emoji-selector.py" -show combi
