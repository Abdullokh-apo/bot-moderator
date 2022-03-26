import docx


doc = docx.Document("C:\\Users\\abdul\\PycharmProjects\\bot_moderator\\censure"
                    "\\плохие слова.docx")

all_paras = doc.paragraphs
paras = [para.text for para in all_paras]
for each_para in paras:
    all = str(each_para).split(', ')
