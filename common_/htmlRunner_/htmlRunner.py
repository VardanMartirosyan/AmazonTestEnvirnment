from common_.htmlRunner_.sources import htmlTestRunner
import datetime
from pathlib import Path


class HtmlRunner():
    def __get_prj_root_dir_name(self):
        command = "Path(__file__).absolute()"
        while True:
            rootDir = str(eval(command))
            if rootDir.split(sep="\\")[-1] == "AmazonTestEnvirnment":
                return rootDir
            else:
                command += ".parent"

    def get_report_file_name(self):
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime('%d-%m-%Y_%H-%M-%S')
        reportFileName = f"html_report_{formatted_datetime}.html"
        return reportFileName

    def get_html_runner(self, title='Test Report'):
        prjRoot = self.__get_prj_root_dir_name()
        outfile = open(prjRoot + "\_reports_\\" + self.get_report_file_name(), "wb")
        runner = htmlTestRunner.HTMLTestRunner(
            stream=outfile,
            title=title,
            description='Random_suite_tests'
        )

        return runner
