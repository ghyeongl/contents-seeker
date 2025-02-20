#!/usr/bin/env python3
import os

def seeker(root_dir='.', output_file='codes.txt'):
    """
    root_dir부터 시작하여 모든 하위 디렉토리까지 탐색하면서
    확장자가 .py 또는 .js인 파일을 찾되,
    1) node_modules 디렉토리는 탐색에서 제외하고
    2) seeker.py 파일도 제외한다.
    찾은 파일들의 경로와 파일 내용을 화면과 output_file에 출력/저장.
    """
    with open(output_file, 'w', encoding='utf-8') as out:
        for current_path, dirs, files in os.walk(root_dir):
            # 1) node_modules 폴더는 탐색에서 제외
            if 'node_modules' in dirs:
                dirs.remove('node_modules')

            for file_name in files:
                # 2) seeker.py 파일은 스킵
                if file_name == 'seeker.py':
                    continue

                if file_name.endswith('.py') or file_name.endswith('.js'):
                    full_path = os.path.join(current_path, file_name)

                    # 경로명 출력 + 파일에 기록
                    print(full_path)
                    out.write(full_path + '\n')

                    # 파일 내용 읽고 출력 + 파일에 기록
                    try:
                        with open(full_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            print(content)
                            out.write(content + '\n')
                    except Exception as e:
                        msg = f"파일을 열 수 없습니다: {e}"
                        print(msg)
                        out.write(msg + '\n')

def main():
    seeker(root_dir='.', output_file='codes.txt')

if __name__ == "__main__":
    main()
