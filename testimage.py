import requests
import json
from data_change import save_image_info_to_excel



def create_iamge(prompt,size):
    url = "https://api.siliconflow.cn/v1/black-forest-labs/FLUX.1-schnell/text-to-image"

    payload = {
        #"prompt": "Vincent van Gogh style, a swirling celestial sky, with vibrant stars and a sense of cosmic depth.",
        "prompt": prompt,
        "image_size": size, #1024x576,1024x1024,576x1024,576x1024
        "num_inference_steps": 20
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer sk-aylemansytmfkvcjaropqidniqveurodcdsscxldwnkmmcgw"
    }

    response = requests.post(url, json=payload, headers=headers)

    # 将字符串解析为JSON（字典）
    data = json.loads(response.text)
    print(data)
    # 访问images列表中第一个元素的url
    image_url = data['images'][0]['url']
    save_image_info_to_excel(image_url,user="",size=size)
    #print(response.text)
    return image_url 

'''
{
  "images": [
    {
      "url": "https://sf-maas-uat-prod.oss-cn-shanghai.aliyuncs.com/outputs/de17f4b6-1fed-4f37-b6f7-94d3d441f137_00001_.png"
    }
  ],
  "timings": {
    "inference": 4.883
  },
  "shared_id": "0"
}

'''
prompt1="A beautiful princess,slightly bend and lower head + perfect face + pale red lips,Ultraviolet,Charlie Bowater style,Paper,The composition mode is Waist shot style,Hopeful,Octane render,4k HD"
prompt2= "Moulin Rouge, cabaret style, burlesque, photograph of a gorgeous beautiful woman, slender toned body, at a burlesque club, highly detailed, posing, smoky room, dark lit, low key, alluring, seductive, muted colors, red color pop, rim light, lingerie, photorealistic, shot with professional DSLR camera, F1. 4, 1/800s, ISO 100"
prompt3 = "A dynamic portrait of a female journalist at the Olympic Games, wearing a 'Beijing News' press badge around her neck and holding a microphone in her hand, capturing the essence of live reporting."
prompt4 = "and raised with a microphone, capturing the intensity of live sports reporting. With a determined expression and focused gaze, she embodies professionalism and enthusiasm. The scene is set against the vibrant backdrop of the Olympic venue, filled with the energy of competition and the anticipation of the crowd. The composition is a dynamic waist shot, showcasing her stance and the microphone as the central focus. The mood is hopeful and expectant, as she awaits the next big moment to report. Rendered in the distinctive style of photojournalism, with a touch of artistic flair, the image is crisp and clear in 4k HD quality."
prompt5 = "A confident and eloquent professional woman with wavy long hair framing her shoulders, her face lit by a warm, flattering stage light that highlights her engaging smile, the creases at the corners of her eyes, and the charming dimples beside her lips. The fine, wispy strands of hair add texture and authenticity to the portrait. Captured in a medium close-up shot from a slightly elevated angle, the perspective emphasizes her commanding presence on stage. The Google badge around her neck is clearly visible, grounding the image in a recognizable corporate setting. The lighting is expertly crafted to create depth and contrast, drawing attention to her expressive face and the moment of connection with her audience. The image is rendered with high fidelity, in crisp 4k high-definition quality"
prompt6 ="A confident and eloquent professional woman with wavy long hair framing her shoulders, her face illuminated by the warm, flattering stage lights that accentuate her engaging smile, the fine lines at the corners of her eyes, and the charming dimples beside her lips. The subtle strands of loose hair add a touch of natural authenticity to the portrait. Captured in a mid-shot that includes the background environment, the perspective captures her commanding presence on stage while also providing context to the setting. The Google badge around her neck is clearly visible, anchoring the image in a recognizable corporate setting. The lighting is expertly crafted to create depth and contrast, drawing attention to her expressive face and the moment of connection with her audience. The image is rendered with high fidelity, in crisp 4k high-definition quality, ensuring that every detail, from the foreground to the background, is captured with clarity and precision."
prompt7 ="A charismatic and accomplished professional woman, with her wavy long hair cascading over her shoulders, stands confidently at a TED Talk podium. Her face, beaming with a genuine, toothy smile, is softly illuminated by the stage lights, revealing the delicate creases at the corners of her eyes and the endearing dimples that form when she smiles. The subtle, stray wisps of hair lend an air of authenticity and approachability to her image. In the mid-shot composition, she occupies two-thirds of the frame, allowing the iconic TED Talk backdrop to be prominently featured, enhancing the prestige of the setting. The Google badge around her neck is clearly visible, signifying her affiliation with a leading tech giant. The lighting is meticulously designed to create a sense of depth, with highlights and shadows that draw the viewer's attention to her expressive features and the engaging narrative she's delivering. The image is rendered with exceptional clarity and detail in 4k high-definition, ensuring that every nuance of the scene, from the texture of her hair to the ambiance of the TED Talk venue, is captured with precision."
prompt8 = "A poised and articulate professional woman with wavy long hair that elegantly frames her shoulders is delivering a compelling speech at a TED Talk event. Her radiant smile, with its toothy expression, is accentuated by the stage lighting, which also highlights the fine lines at the corners of her eyes and the charming dimples in her cheeks. The delicate strands of loose hair add a natural and authentic touch to her appearance. In this mid-shot composition, she occupies precisely half of the frame, offering a balanced view that includes the distinctive TED Talk backdrop, which contributes to the prestigious atmosphere of the scene. The Google badge on her neck is prominently visible, indicating her association with a renowned tech company. The lighting is expertly crafted to create a dramatic effect, with strategic highlights and shadows that draw attention to her expressive face and the passion of her speech. The image is rendered in high-resolution 4k quality, ensuring that every detail, from the texture of her hair to the nuances of the TED Talk environment, is captured with exceptional clarity and precision."
prompt9 ="A confident and articulate professional woman with wavy long hair that elegantly frames her shoulders is featured in the midst of an engaging TED Talk. Her genuine smile, marked by the subtle creases at the corners of her eyes and the dimples in her cheeks, is illuminated by the thoughtfully arranged stage lighting. The loose strands of hair lend a sense of authenticity and approachability to her image. Within this composition, she occupies a quarter of the frame, allowing the iconic TED Talk backdrop to dominate the scene and convey the significance of the event. The Google badge on her neck is still clearly visible, denoting her affiliation with a leading tech entity. The lighting design is such that it casts a dramatic spotlight on her, creating a stark contrast with the surrounding environment and drawing the viewer's focus to her expressive face and the power of her speech. The image is rendered in crisp 4k high-definition quality, ensuring that every detail, from the texture of her hair to the ambiance of the TED Talk venue, is captured with clarity and precision."
prompt10 = "A poised and articulate professional woman with wavy long hair is delivering a captivating TED Talk, her presence commanding the stage. Her smile, a blend of warmth and professionalism, is accentuated by the stage lights that play on the subtle creases at the corners of her eyes and the dimples in her cheeks. The loose strands of hair add a natural touch to her composed appearance. In this long-shot composition, she occupies a smaller portion of the frame, allowing the full grandeur of the TED Talk venue to come into view. The audience, the stage setup, and the iconic TED logo are all visible, creating a sense of scale and importance. The Google badge on her neck is a subtle detail that signifies her association with innovation and technology. The lighting is masterfully used to create a dramatic effect, with highlights and shadows that draw attention to her, yet do not overshadow the significance of the TED stage. The image is rendered in high-resolution 4k quality, capturing every detail with clarity, from the individual strands of hair to the collective energy of the audience."
prompt11 ="In a long-shot composition, a professional woman with wavy long hair is immersed in her speech at a TED Talk event. Her animated expression and the subtle creases at the corners of her eyes, along with the dimples in her cheeks, are illuminated by the stage lights, reflecting her passion and engagement with the audience. The loose strands of hair suggest a moment of movement and energy. Occupying a quarter of the frame, she is framed against the backdrop of the TED Talk venue, with the audience and stage setup visible, emphasizing the scale and significance of the event. The Google badge on her neck stands out as a symbol of her affiliation with a leading tech company. The lighting is strategically used to highlight her presence while also casting a warm glow over the entire scene, capturing the essence of the live speech. The image is rendered in sharp 4k high-definition quality, ensuring that every detail, from the texture of her hair to the attentive faces of the audience, is captured with vivid clarity."
prompt12 ="A dynamic TED Talk unfolds in a far-shot composition, capturing the full expanse of the stage and the attentive audience. At the center, a professional woman with wavy long hair is in the midst of her speech, her figure a beacon of eloquence. Her animated gestures and the lively expressions on her face, marked by the creases at the corners of her eyes and the dimples in her cheeks, are accentuated by the strategic stage lighting. The loose strands of hair suggest the vigor of her delivery. Despite the far-shot perspective, she remains the focal point, occupying a quarter of the frame and drawing the viewer's gaze. The Google badge on her neck is a subtle but clear indicator of her association with a leading tech entity. The backdrop of the TED Talk venue, with its iconic elements and the engaged audience, provides context and amplifies the significance of the moment. The lighting design bathes the scene in a warm glow, enhancing the liveliness of the event and the woman's commanding presence. The image is rendered in crisp 4k high-definition quality, ensuring that every detail, from the contours of the stage to the nuances of the audience's reactions, is captured with precision and clarity."
#url1 = create_iamge(prompt12)
#"Picasso's cubist style, reimagining stars with geometric shapes and abstract forms.")
#print(url1)