all: report.pdf 

report.pdf: report.tex report.bib images/speedup1.pdf images/mcs.pdf images/restart_speedup1.pdf images/useful.pdf
	pdflatex -halt-on-error report.tex
	bibtex report
	pdflatex -halt-on-error report.tex
	pdflatex -halt-on-error report.tex
