from django import template

register = template.Library()

@register.filter(name='class')
def add_classes(value, arg):
  css_classes = value.field.widget.attrs.get('class', '')

  if css_classes:
    css_classes = css_classes.split(' ')
  else:
    css_classes = []

  args = arg.split(' ')
  for a in args:
    if a not in css_classes:
      css_classes.append(a)

  return value.as_widget(attrs={'class': ' '.join(css_classes)})


@register.filter(name='mask')
def mask(value, mask_type):
  """ Mask String value """
  if mask_type == 'phone':
    if len(value) == 10:
      return "(%s%s) %s%s%s%s-%s%s%s%s" % tuple(value)
    elif len(value) == 11:
      return "(%s%s) %s %s%s%s%s-%s%s%s%s" % tuple(value)


  return value
