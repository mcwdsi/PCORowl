all:
	@echo "Available commands:"
	@echo "reload"
	@echo "restart"
	@echo "query(1-13)"
	@echo "edit"
	@echo "about"

about: 
	@echo "This Makefile is designed to speed up development with Stardog."
	@echo "Place the Makefile in the stardog/bin directory and run it from there. Note that the "
	@echo "Makefile assumes your PCORowl directory is located at the same level as your stardog directory."

reload:
	@echo "Reloading PCORowl."	
	./stardog-admin virtual remove PCORowl
	./stardog-admin virtual add ../../PCORowl/stardog_config/PCORowl.properties ../../PCORowl/stardog_config/PCORowl.ttl

restart:
	@echo "Restarting stardog server."
	./stardog-admin server stop
	./stardog-admin server start

query1:
	$(call run_query,1)
query2:
	$(call run_query,2)
query3:
	$(call run_query,3)
query4:
	$(call run_query,4)
query5:
	$(call run_query,5)
query6:
	$(call run_query,6)
query7:
	$(call run_query,7)
query8:
	$(call run_query,8)
query9:
	$(call run_query,9)
query10:
	$(call run_query,10)
query11:
	$(call run_query,11)
query12:
	$(call run_query,12)
query13:
	$(call run_query,13)
query14:
	$(call run_query,14)
edit:
	vim ../../PCORowl/stardog_config/PCORowl.ttl

define run_query
	time ./stardog query PCORnet ../../PCORowl/stardog_config/queries/query$(1).rq
	@head -n1 ../../PCORowl/stardog_config/queries/query$(1).rq
endef
