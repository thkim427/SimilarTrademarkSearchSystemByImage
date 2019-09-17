# turicreate 설치
!pip install turicreate

# turicreate 사용
import turicreate as tc

#이미지 폴더를 데이터 모델로 객체화
reference_data = tc.image_analysis.load_images('img') #이미지 폴더 경로 지정                       
reference_data = reference_data.add_row_number()

#객체화 한 이미지 모음을 Sframe으로 저장
reference_data.save('final.sframe') #저장 폴더 이름, 경로 지정


#해당되는 Sframe을 모델로 객체화
model = tc.image_similarity.create(reference_data)

#모델을 로컬 파일로 저장
model.save('final_model') #저장 폴더 이름, 경로 지정


                                                
                                                
                                                
                                                