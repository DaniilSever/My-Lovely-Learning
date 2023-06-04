from courses.models import Lesson

def recently_viewed(request, course_pk):
    if "recently_viewed_courses" not in request.session:
        request.session["recently_viewed_courses"] = [course_pk]
    else:
        if course_pk in request.session["recently_viewed_courses"]:
            request.session["recently_viewed_courses"].remove(course_pk)
        request.session["recently_viewed_courses"].insert(0, course_pk)
        if len(request.session["recently_viewed_courses"]) > 6:
            request.session["recently_viewed_courses"].pop()

def last_passed_lesson(request, course_pk, lesson_pk, get=False):
    c = f"last_lesson_{course_pk}"
    
    if c not in request.session:
        first_lesson = Lesson.objects.filter(subchapter__chapter__course__pk=course_pk)\
            .order_by('subchapter__chapter_order').first()
        request.session[c] = lesson_pk
    else:
        if not get:
            request.session[c] = lesson_pk
        return request.session[c]