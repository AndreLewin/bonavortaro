from django import template

register = template.Library()


@register.filter
def boneckoloro(value):
    """Donas la kolortonon de la boneco de la Radiko/Propono"""
    kolortono = 120*(value)
    return "hsl(" + str(kolortono) + " , 100%, 40%)"