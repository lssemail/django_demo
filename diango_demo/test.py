from baidu_face_search.models import baidu_face_search


if __name__ == '__main__':

    lession_id = '65db4c1d77e84ffaadb66ba4dc87d1cf'
    stu_no = '20140076'
    score = 45
    user_id = '20140049'
    error_code = '0'
    error_msg = 'SUCCESS'

    result = baidu_face_search.save(lession_id, stu_no, score, user_id, error_code, error_msg)
    print(result)