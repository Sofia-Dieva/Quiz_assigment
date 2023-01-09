from .models import Answer, Question, Quiz
from nested_admin.nested import NestedTabularInline, NestedModelAdmin
from django.contrib import admin
from django import forms


class AnswerInlineFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form['is_right_answer'].data:
                count += 1
        if count < 1 or count == len(self.forms):
            raise forms.ValidationError('You must have at least one order')


class AnswerInline(NestedTabularInline):
    model = Answer
    extra = 2
    formset = AnswerInlineFormset


class QuestionInline(NestedTabularInline):
    model = Question
    inlines = [AnswerInline]
    extra = 1


@admin.register(Quiz)
class QuizAdmin(NestedModelAdmin):
    inlines = [QuestionInline]
