import requests
text = "Aapke drishtikon par upasthiti neetiyon ke prati vichaarshil hai. Main chhatra sangathan aur bhagidari sunischit karne ke mahatva ko samajhta hoon, lekin aapka tippani deta hai ki shiksha settings mein sahanubhooti aur lachilapan ki avashyakta hai. Yeh mahatvapurn hai ki chhatron ke samne vibhinn chunautiyon ko manyata di jaye jo unki upasthiti par prabhav daal sakti hain, aur kathin neetiyon se tanav ko badha sakti hain aur shiksha ko badhit kar sakti hain. Samjhane aur samarthan pradan karke, sansthan ek aur sankranti shiksha vaatavaran bana sakte hain jahan chhatra mulyankan aur safalta ke liye mahsus karte hain. Dhanyavad ki aapne is mahatvapurn charcha ko prerit kiya hai ki hum chhatron ki samagr kalyan ki samarthan mein kaise behtar saksham ho sakte hain jabki shiksha manakon ko banaye rakhte hain."

api_url = 'https://api.api-ninjas.com/v1/sentiment?text={}'.format(text)
response = requests.get(api_url, headers={'X-Api-Key': '9No6wnmZqzRC/NRH0VvxHA==QRYgA94Njvme77Wg'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)

