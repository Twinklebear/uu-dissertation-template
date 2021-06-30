# Dissertation Template

This slightly modified version of the dissertation template
corrects some issues with title spacing and is configured
to use the IEEE TVCG style for figure/table references and
the bibliography. Tell the thesis editor you are using
the IEEE TVCG style when you submit if you don't modify that
part of the template. **There are still other rules about layout
and structure required by the thesis office this template
doesn't/can't enforce**. See the [Thesis handbook](https://gradschool.utah.edu/thesis/handbook/) for information
about figure placement, reference ordering, title lengths,
etc.
To simplify getting your dissertatio through the thesis office,
I **strongly** recommend you just put all the figures at the end
of each chapter. You can send to your committee for review with the
figures inline, but for the final version it's much easier to just
put them all at the end of each chapter.

You'll want to fill in your committee, department info and
so on in the dissertation.tex (comes after the title).

## Using the Makefile

You can run `make` to compile the PDF of your dissertation.
This will run pdflatex, bibtex, then pdflatex twice to populate
cross references. This can take some time so you can also run
`make fast` to just run pdflatex. To build a compressed version
of your dissertation for email or submission to the thesis
office you can run `make compress`.

## Abbreviating your Bibliograpy

The script `scripts/abbreviate_bibs.py` can be run on your bib files
to replace any long words with the corresponding abbreviations
based on the IEEE style. It will also abbreviate months.
The script will also enforce proper lower casing of titles as
well as it can.
If your bib contains some special latex commands or characters
(e.g., `\textemdash`) they may be made invalid by this script.
For example a title like `{OSPRay}\textemdash{A} {Ray} {Tracing}`
will be turned into `{OSPRay}\textemdashA Ray Tracing` to enforce
lower casing of the title. However, this produces the invalid latex
command `\textemdashA`, which you need to manually correct
to `\textemdash{}A`. I recommend running this script only when your
bibliography is complete and you are working on populating final missing
things (months, page numbers, etc.) and polishing the formatting.

## Note about Table of Contents

The dissertation.tex file sets the table of content depth to 3.
Chris Pickett recommends this for expedited service from the
thesis office if you have many subheading levels.

## Note about List of Figures and Tables

The thesis office has some rules about when a list of figures and
tables is required or optional, based on how many of them you
have. Check the thesis office for this info, and if it's optional
you can remove it by commenting out the `\listoffigures` or
`\listoftables` in `dissertation.tex` as desired.

