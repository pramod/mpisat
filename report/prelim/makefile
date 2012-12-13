all: report.pdf 

report.pdf: report.tex report.bib images/speedup1.pdf
	pdflatex -halt-on-error report.tex
	bibtex report
	pdflatex -halt-on-error report.tex
	pdflatex -halt-on-error report.tex
