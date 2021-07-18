from django import template

register = template.Library()


@register.filter()
def range(min):
    return range(min)

@register.filter()
def get_param_val(obj, cnt):
    if(cnt==1):
        return obj.get_first_param_val_display()
    elif(cnt==2):
        return obj.get_second_param_val_display()
    elif(cnt==3):
        return obj.get_third_param_val_display()
    elif(cnt==4):
        return obj.get_fourth_param_val_display()


@register.filter()
def get_param_db_val(obj, cnt):
    if(cnt==1):
        return obj['first_param_val'].value()
    elif(cnt==2):
        return obj['second_param_val'].value()
    elif(cnt==3):
        return obj['third_param_val'].value()
    elif(cnt==4):
        return obj['fourth_param_val'].value()

@register.filter()
def get_param_form(obj):
    return obj[1:]

@register.filter()
def get_meeting_no(cnt):
    if cnt == 1:
        return "3rd"
    else:
        return str(2+cnt)+"th"
