from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options


def upload(file, canvas_id, canvas_ps):
    options = Options()
    options.add_argument('--headless')
    dr = webdriver.Chrome(chrome_options=options)

    print('open')
    dr.get('https://canvasworkspace.brother.com/jp/')
    try:
        print('input id')

        dr.execute_script(
            "document.querySelector('#UserName').value = '" + canvas_id + "'")

        print('input password')
        dr.execute_script(
            "document.querySelector('#Password').value = '" + canvas_ps + "'")

        print('click login button')
        dr.execute_script(
            "document.querySelector('#loginForm > section > form \
            > div:nth-child(6) > button').click()"
        )

        print('click new item button')
        dr.execute_script(
            "document.querySelector('#cpcontainer > \
            div.box.box0.cp.create.masonry-brick > div').click()"
        )

        print('typing project name')
        dr.execute_script(
            "document.querySelector('#canvas_title').value = 'title'")

        print('click svg file button')
        dr.execute_script("document.querySelector('#tool_importvec').click()")

        print('select import file')
        dr.find_element_by_css_selector('#importfile').send_keys(file)

        print('click ok button')
        dr.execute_script("document.querySelector('#import_wiz_ok').click()")

        sleep(10)

        try:
            # OKクリック(データフォーマットが大きいので縮小してインポートしました)
            print('click ok')
            dr.execute_script(
                "document.querySelector('body > div:nth-child(32) > \
                div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix \
                > div > button').click()")
        except Exception:
            # this is not error
            print('skip')

        print('click overwrite save')
        dr.execute_script("document.querySelector('#tool_save').click()")

        print('click ok button')
        dr.execute_script("document.querySelector('#savadlg-close').click()")

        sleep(4)

        print('complete!!')
        print('https://canvasworkspace.brother.com/jp/Home?show=myproj')

    except Exception:
        raise Exception

    finally:
        dr.quit()
