from django import template


register = template.Library()


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def preview(value, x):
   """
   value: значение, к которому нужно применить фильтр
   """
   # Возвращаемое функцией значение подставится в шаблон.
   if len(value) > x:
      return value[0:x] + '...'
   else:
      return value


@register.filter()
def readability(value):
   return value.strftime('%d.%m.%Y %H:%M:%S')

@register.filter()
def readability_2(value):
   return value.strftime('%d.%m.%Y')


@register.filter()
def censor(text: str):
   if not isinstance(text, str):
      raise ValueError("Передаваемый аргумент должен быть строкой")
   black_list = [
      'rediska',
      'random',
      'kakawka',
      'россии'
   ]

   words = text.split()
   censored_text = []
   for word in words:
      if word.lower() in black_list:
         censored_text.append(word[0] + '*' * len(word[1:]))
      else:
         censored_text.append(word)
   return ' '.join(censored_text)






