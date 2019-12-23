from mailmerge import MailMerge

doc = MailMerge("./Ex44_file/test.docx")
doc.merge(
    username="ddu",
    clazz="17计算机科学与技术"
)

doc.write("./Ex44_file/res.docx")