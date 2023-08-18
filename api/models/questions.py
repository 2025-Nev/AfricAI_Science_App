from typing import List


class Question:
    def __init__(self, question_text: str, answer_choices: List[str], correct_answer: str):
        self.question_text = question_text
        self.answer_choices = answer_choices
        self.correct_answer = correct_answer

    def is_answer_correct(self, answer: str) -> bool:
        """Returns True if the given answer is correct for this question, False otherwise."""
        return answer == self.correct_answer

    def get_questions() -> List[Question]:
        """
        Returns a list of questions.
        """
        questions_data = [
            {
                "question": "Which large mammal is known for its distinctive tusks and is native to African savannas?",
                "options": ["Giraffe", "Lion", "Elephant", "Zebra"],
                "answer": "Elephant"
            },
            {
                "question": "What is the fastest land animal and is found in the grasslands of Africa?",
                "options": ["Cheetah", "Hippopotamus", "Gorilla", "Leopard"],
                "answer": "Cheetah"
            },
            {
                "question": "Which large mammal is known for its distinctive tusks and is native to African savannas?",
                "options": ["Giraffe", "Lion", "Elephant", "Zebra"],
                "answer": "Elephant"
            },
            {
                "question": "What is the fastest land animal and is found in the grasslands of Africa?",
                "options": ["Cheetah", "Hippopotamus", "Gorilla", "Leopard"],
                "answer": "Cheetah"
            },
            {
                "question": "Which species of ape is found in the forests of Central and West Africa, known for its intelligence and tool-making abilities?",
                "options": ["Baboon", "Chimpanzee", "Orangutan", "Gorilla"],
                "answer": "Chimpanzee"
            },
            {
                "question": "What is the national bird of Kenya, known for its vibrant red and blue plumage?",
                "options": ["Secretary Bird", "African Grey Parrot", "Lilac-breasted Roller", "Ostrich"],
                "answer": "Lilac-breasted Roller"
            },
            {
                "question": "Which large carnivore is known for its distinctive black mane and is often referred to as the 'King of the Jungle'?",
                "options": ["Leopard", "Cheetah", "Hyena", "Lion"],
                "answer": "Lion"
            },
            {
                "question": "Which animal, known for its unique stripes, is native to African grasslands and is often associated with the Serengeti?",
                "options": ["Giraffe", "Zebra", "Elephant", "Rhino"],
                "answer": "Zebra"
            },
            {
                "question": "What is the largest land animal on Earth, characterized by its long neck and legs?",
                "options": ["Giraffe", "Hippopotamus", "African Elephant", "Gorilla"],
                "answer": "Giraffe"
            },
            {
                "question": "Which aquatic mammal is found in African rivers, is known for its aggressive nature, and has large jaws and teeth?",
                "options": ["Dolphin", "Manatee", "Hippopotamus", "Seal"],
                "answer": "Hippopotamus"
            },
            {
                "question": "What is the fastest marine animal and is known for its powerful jumps and acrobatics?",
                "options": ["Shark", "Dolphin", "Sea Turtle", "Sailfish"],
                "answer": "Dolphin"
            },
            {
                "question": "Which large herbivore is known for its distinctive hump and is adapted to desert life?",
                "options": ["Buffalo", "Camel", "Giraffe", "Rhinoceros"],
                "answer": "Camel"
            },
            {
                "question": "Which African country is known as the 'Land of a Thousand Hills'?",
                "options": ["Rwanda", "Uganda", "Kenya", "Tanzania"],
                "answer": "Rwanda"
            },
            {
                "question": "What is the highest mountain in Africa and one of the Seven Summits?",
                "options": ["Mount Kilimanjaro", "Mount Kenya", "Mount Elgon", "Simien Mountains"],
                "answer": "Mount Kilimanjaro"
            },
            {
                "question": "Which desert, located in North Africa, is one of the hottest and largest deserts in the world?",
                "options": ["Namib Desert", "Kalahari Desert", "Sahara Desert", "Danakil Desert"],
                "answer": "Sahara Desert"
            },
            {
                "question": "Which river is the longest in the world and flows through several African countries?",
                "options": ["Congo River", "Nile River", "Niger River", "Zambezi River"],
                "answer": "Nile River"
            },
            {
                "question": "Which African country is located at the crossroads of East Africa and is bordered by Kenya, Tanzania, and Uganda?",
                "options": ["Ethiopia", "Burundi", "Rwanda", "South Sudan"],
                "answer": "Burundi"
            },
            {
                "question": "What is the largest lake in Africa and the second-largest freshwater lake by surface area in the world?",
                "options": ["Lake Victoria", "Lake Tanganyika", "Lake Malawi", "Lake Chad"],
                "answer": "Lake Victoria"
            },
            {
                "question": "Which island nation located in the Indian Ocean is known for its lemurs and unique biodiversity?",
                "options": ["Mauritius", "Madagascar", "Seychelles", "Comoros"],
                "answer": "Madagascar"
            },
            {
                "question": "Which African country is home to the city of Timbuktu and was historically a center of learning and trade?",
                "options": ["Mali", "Niger", "Chad", "Senegal"],
                "answer": "Mali"
            },
            {
                "question": "Which strait connects the Red Sea to the Gulf of Aden and separates Africa from the Arabian Peninsula?",
                "options": ["Strait of Hormuz", "Strait of Gibraltar", "Strait of Malacca", "Strait of Bab-el-Mandeb"],
                "answer": "Strait of Bab-el-Mandeb"
            },
            {
                "question": "Which African country is known as the 'Pearl of Africa' and is home to a diverse range of wildlife and landscapes?",
                "options": ["Uganda", "Kenya", "Tanzania", "Zimbabwe"],
                "answer": "Uganda"
            },
            {
                "question": "Which West African country is known for its vibrant Kente cloth, often worn during special occasions?",
                "options": ["Nigeria", "Ghana", "Senegal", "Mali"],
                "answer": "Ghana"
            },
            {
                "question": "What is the name of the traditional African musical instrument that consists of wooden bars struck with mallets?",
                "options": ["Djembe", "Mbira", "Balafon", "Kora"],
                "answer": "Balafon"
            },
            {
                "question": "Which African dance style, characterized by fast footwork and rhythmic movements, originated in South Africa?",
                "options": ["Salsa", "Samba", "Hula", "Gumboot Dance"],
                "answer": "Gumboot Dance"
            },
            {
                "question": "Which North African country is known for its unique blue-painted city, often referred to as the 'Blue Pearl'?",
                "options": ["Morocco", "Algeria", "Tunisia", "Mauritania"],
                "answer": "Morocco"
            },
            {
                "question": "What is the traditional African storytelling device that often uses intricate patterns and symbols to convey messages?",
                "options": ["Drum", "Adinkra", "Talking Stick", "Didgeridoo"],
                "answer": "Adinkra"
            },
            {
                "question": "Which East African tribe is known for their intricate beadwork and colorful clothing?",
                "options": ["Zulu", "Maasai", "Himba", "Kikuyu"],
                "answer": "Maasai"
            },
            {
                "question": "What is the name of the traditional South African dish that consists of minced meat and spices, often served in a hollowed-out loaf of bread?",
                "options": ["Injera", "Bobotie", "Fufu", "Jollof Rice"],
                "answer": "Bobotie"
            },
            {
                "question": "Which West African city is famous for its bustling markets, historic forts, and rich history as a major trading hub?",
                "options": ["Accra", "Lagos", "Dakar", "Cairo"],
                "answer": "Accra"
            },
            {
                "question": "What is the name of the traditional African mask that represents a protective spirit and is often used in ceremonies?",
                "options": ["Hannya", "Bwa", "Fang", "Bwa"],
                "answer": "Fang"
            },
            {
                "question": "Which form of oral poetry, often performed with musical accompaniment, is a major cultural tradition in West Africa?",
                "options": ["Haiku", "Limerick", "Rap", "Griot"],
                "answer": "Griot"
            },
            {
                "question": "Which African country was the birthplace of Nelson Mandela and played a significant role in the fight against apartheid?",
                "options": ["Zimbabwe", "Namibia", "South Africa", "Mozambique"],
                "answer": "South Africa"
            },
            {
                "question": "Which African nation was the first to gain independence from European colonial rule in 1951?",
                "options": ["Ghana", "Kenya", "Nigeria", "Algeria"],
                "answer": "Ghana"
            },
            {
                "question": "Which African leader, also known as the 'Lion of Judah,' was the Emperor of Ethiopia and resisted Italian colonization?",
                "options": ["Patrice Lumumba", "Kwame Nkrumah", "Haile Selassie", "Jomo Kenyatta"],
                "answer": "Haile Selassie"
            },
            {
                "question": "Which African country is known for its policy of apartheid, a system of racial segregation and discrimination?",
                "options": ["Nigeria", "Zimbabwe", "South Africa", "Uganda"],
                "answer": "South Africa"
            },
            {
                "question": "Which West African country was founded by freed slaves from the United States and declared its independence in 1847?",
                "options": ["Liberia", "Sierra Leone", "Gambia", "Senegal"],
                "answer": "Liberia"
            },
            {
                "question": "Who was the first female president in Africa and became the president of Liberia in 2006?",
                "options": ["Ellen Johnson Sirleaf", "Joyce Banda", "Amina Mohamed", "Nkosazana Dlamini-Zuma"],
                "answer": "Ellen Johnson Sirleaf"
            },
            {
                "question": "Which African country underwent a peaceful transition from apartheid to majority rule, led by Nelson Mandela?",
                "options": ["Kenya", "Zimbabwe", "Nigeria", "South Africa"],
                "answer": "South Africa"
            },
            {
                "question": "Which African leader, also known as 'Madiba,' was imprisoned for 27 years before becoming the first black president of South Africa?",
                "options": ["Patrice Lumumba", "Kwame Nkrumah", "Nelson Mandela", "Jomo Kenyatta"],
                "answer": "Nelson Mandela"
            },
            {
                "question": "Which North African country experienced a revolution in 2011, known as the Arab Spring, resulting in the overthrow of its long-serving leader?",
                "options": ["Tunisia", "Algeria", "Morocco", "Libya"],
                "answer": "Tunisia"
            },
            {
                "question": "Which African leader was a founding father of the African Union (AU) and the first Prime Minister and President of Ghana?",
                "options": ["Kwame Nkrumah", "Nelson Mandela", "Haile Selassie", "Jomo Kenyatta"],
                "answer": "Kwame Nkrumah"
            },
        ]

        questions = []
        for question_data in questions_data:
            question = Question(
                question_data["question"],
                question_data["options"],
                question_data["answer"]
            )
        questions.append(question)

        return questions
