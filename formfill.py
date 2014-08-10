import mechanize

# fills a google spreadsheet form based on a given dict.
def fill_form(forminput, url):
    br = mechanize.Browser()
    br.open(url)

    for form in br.forms():
        if form.attrs['id'] == 'ss-form': # google spreadsheet form
            br.form = form
            break

    print br.attrs
    print br.controls

    for c in br.controls:
        if 'aria-label' in c.attrs:
            field_name = str.strip(c.attrs['aria-label'])
            if field_name in forminput:
                c.value = str(forminput[field_name])

        print c.attrs

    br.submit()
