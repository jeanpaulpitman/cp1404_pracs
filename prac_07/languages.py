"""CP1404/CP5632 Practical - Programming languages."""
from prac_07.programming_language import ProgrammingLanguage


def main():
    """Main."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(visual_basic)

    languages = [ruby, python, visual_basic]
    print("The Dynamic typed languages are:")
    # print([language.name for language in languages if language.is_dynamic()])
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
