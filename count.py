"""统计词频"""


def count_words(s, n):
    """返回字符串s中出现频率最高的n个词."""

    s_list = s.lower().split(' ')  # 单词统一转换为小写形式，并以空格进行切分

    # 统计字符串s中每个单词出现的次数
    top_n_dict = {}
    for word in s_list:
        if word in top_n_dict:
            top_n_dict[word] += 1
        else:
            top_n_dict[word] = 1

    # 按照出现频次对单词进行排序，如果出现频次相同，则按字母顺序排序
    word_frequency = []
    values = sorted(list(set(top_n_dict.values())), reverse=True)  # 统计所有单词出现的频次情况，将频次降序放入列表
    for w in values:
        # 将出现频次相同的单词放在一个列表里
        word_list = []
        for k, v in top_n_dict.items():
            if v == w:
                word_list.append((k, v))
        # 将出现频次相同的单词排序后添加到词频列表
        word_frequency.extend(sorted(word_list))

    # 返回出现频次排前n的单词
    return word_frequency[:n]


if __name__ == '__main__':
    text = 'Over several years, as part of its ‘giving back’ philosophy, CodeBlue has supported Ronald McDonald House Auckland with donations, mid-Winter Christmas parties, cook-offs and other events, and sourcing much-needed technology – such as printers, computers and other equipment. As part of this long term relationship and support for Ronald McDonald House Auckland, CodeBlue vendor partner HP has worked with Ronald McDonald House Auckland to identify and resource areas of acute need where technology can make a major difference to the children. HP has over time donated equipment to Ronald McDonald House Auckland for the use of children, their parents and staff, including workstations, big-screen monitors and printers, and tablets – the latter to help create a more integrated, dynamic and fun learning environment for the children. “We try to create an environment in the school that gives the children some respite from the frequently harsh, upsetting and sad realities they are dealing with. We aim for bright, light, engaging, fun, and absorbing. The tablets are an important part of that.” Marion Nevin, a teacher with Northern Health School and the Ronald McDonald House Auckland Unit Leader, says now that they have the tablets, she doesn’t know what they would do without them. “The tablets are an extra tool for me to enhance the children’s learning experience. We are using them to expand and reinforce traditional learning.  And for the children, it’s also an escape.  They love engaging with the tablets – honestly, it makes them want to be here even more. Discovery learning Teaching at the school is a mixture of structured and unstructured. Of necessity, Nevin and her team of teacher aides have to be pretty flexible and cater for a range of ages (typically aged 5-12 but sometimes the teaching group will include both younger and older students), abilities and stages of health – some children are patients and some are siblings of the patients. Nevin says the tablets are integral to the ‘discovery learning’ approach they use at the school: “Discovery learning is a technique of inquiry-based learning that gives the children choices and allows them to lead the way in their own learning. It’s a style that gives children much more freedom but they are still guided in their learning outcomes. The children use the tablets to research and discover answers to questions. And, frequently, they will bring us new questions based on their research that form the basis of a subsequent learning session.” In addition to being used for research, the children can use the tablets to record their findings and give presentations back to their classmates. “The tablets are very interactive and give flexibility and adaptability to any learning situation because they can be used in so many ways to accomplish a huge range of tasks suited to all ages and needs,” Marion Nevin says. “The younger children use the tablets differently to the older ones and will use different applications. We structure our learning programmes accordingly.” The tablets are loaded up with a variety of apps and interactive learning games that are suitable for all ages, including YouTube so children can search for specific YouTube clips related to the learning topic, maths games, alphabet games, spelling, reading, and stories to listen to. The tablets are also used for colourful art projects. Nevin points to the classroom walls, full of bright artwork installations – such as Matariki and Space – which the children looked up on the tablets and then recreated as art. The tablets also enable an integrated, seamless learning experience, Nevin says. Prior to having the tablets, the school had a PC for the children to use for their research but it was in another room. This meant sending the children away from what they were doing with their peers and disrupting the flow of the lesson. With the tablets, this is no longer an issue, as the children can stay where they are and interact with each other while they work. “Everything we do here is geared towards the children, who are often overlooked in the midst of a pretty stressful time. It’s about making life better for the children – both those that are sick and those that are not. Everything we do and learn in the classroom feeds into something else, and the tablets definitely enhance that experience,” Marion Nevin concludes. Spotlight: The tablets in action At the time of writing, the 2015 Rugby World Cup (RWC) is in full swing, and the current learning theme is linked to that. Each child has adopted a country and Nevin and her team have created a ‘fact file’ of age and ability-appropriate worksheets and activities based around the RWC and the countries involved. The children use the tablets to help research their country and find answers to the questions. The younger children are tasked with first putting a list of the RWC countries in alphabetical order and then using the tablet to look up the countries and match them to their flags. For more of a challenge, the children can also look up the language/s spoken in the countries. The older children work through a worksheet with various questions and tasks in relation to their country, for example, the name of the national anthem; the national flower; finding and then drawing the national emblem that appears on the jersey; the official languages spoken; the currency.'
    print(count_words(text, 10))
    print(count_words("betty bought a bit of Butter but the Butter was bitter", 3))
