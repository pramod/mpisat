all: report.pdf report.pdf 

report.pdf: report.tex report.bib
	pdflatex -halt-on-error report.tex
	bibtex report
	pdflatex -halt-on-error report.tex
	pdflatex -halt-on-error report.tex
