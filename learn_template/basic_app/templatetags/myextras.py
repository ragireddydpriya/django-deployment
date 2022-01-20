from django import template

register = template.Library()

@register.filter(name="cut")
def cut(val,args):
    return val.replace(args,'')

# register.filter('cut',cut)