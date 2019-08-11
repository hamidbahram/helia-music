from django import template

register = template.Library()

@register.filter
def date_splitter_1(date, separator='-'):
    # import pdb; pdb.set_trace()
    # ipdp for dbug
    # pip install ipdp 
    # ipdp better than pdp
    return date.strftime(f"%Y{separator}%m{separator}%d")

@register.filter
def render_rating(rating):
    html ='<fieldset class="rating">'
    for i in range(5, 0, -1):
        active = None
        if rating > i:
            active = 'style="color: #FFD700;"'
        html += f'''
            <input type="radio" id="star{i}" name="rating" value={i} /><label class = "full" {active} for="star{i}" title="Sucks big time - 1 star"></label>
            <input type="radio" id="starhalf" name="rating" value="half" /><label class="half" {active} for="starhalf" title="Sucks big time - 0.5 stars"></label>
            '''
    html += '</fieldset>'
    return html