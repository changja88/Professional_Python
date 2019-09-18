# 기본 인코더/디코더
# - 텍스트를 바이트로 혹은 바이트를 텍스트로 변환하기 위해 파이썬 배포본에는 100여 개의 코덱(인코더/디코더)가 포함되어있다.

for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño and La Niña?'.encode(codec), sep='\t')

# 인코딩/디코딩 문제 이해하기
