"""HTML components for displaying messages to the user in a banner format"""
from dash import html


def message_banner(category, message):
    """
    Return a coronavirus dashboard-style changelog banner to be used to communicate to the user
    when the dashboard was last updated.

    See https://coronavirus.data.gov.uk
    """
    return html.Ul(
        html.Li(
            html.Div(
                [
                    html.Strong(
                        category,
                        className="govuk-tag",
                        style={
                            "background": "white",
                            "color": "#1d70b8",
                            "margin": "0 1rem 0 0",
                            "line-height": "initial",
                        },
                    ),
                    message,
                ],
                className="govuk-body-s govuk-!-font-weight-bold govuk-!-margin-bottom-0",
            ),
            className="change-log-banner",
        ),
        className="change-logs govuk-!-padding-left-0 govuk-!-margin-top-1",
    )
