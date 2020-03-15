import json
import logging
from os.path import basename

from jinja2 import Environment, PackageLoader, select_autoescape, exceptions

from reporter.utils import auto_text_highlight

env = Environment(
    loader=PackageLoader("reporter", "templates"),
    autoescape=select_autoescape(["html"]),
)
env.filters["basename"] = basename
env.filters["auto_text_highlight"] = auto_text_highlight


def parse(sarif_file):
    """

    :param sarif_file:
    :return:
    """
    report_data = {}
    with open(sarif_file, mode="r") as report_file:
        try:
            report_data = json.loads(report_file.read())
        except json.decoder.JSONDecodeError:
            logging.warning("Unable to parse sarif file {}".format(sarif_file))
            return None
        return report_data


def render_html(report_data, out_file):
    """

    :param report_data:
    :return:
    """
    template = env.get_template("sast-report.html")
    try:
        results = report_data.get("runs")[-1].get("results")
        key_issues = [r for r in results if r.get("level") == "error"]
        if len(key_issues) > 4:
            key_issues = key_issues[:4]
        report_html = template.render(report_data, key_issues=key_issues)
    except exceptions.TemplateSyntaxError as te:
        logging.warning(te)
        return None
    if out_file:
        with open(out_file, mode="w") as fp:
            fp.write(report_html)
            logging.debug("Report written to {}".format(report_html))
    return report_html
