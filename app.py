# Import dependencies
import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins
from shiny import reactive, render, req
import seaborn as sns
import pandas as pd

# Get the data
penguins_df = palmerpenguins.load_penguins()

# Define user interface
ui.page_opts(title="Penguin Data - Breum", fillable=True)

# Add a Shiny UI sidebar for user interaction
with ui.sidebar(open="open"):
    ui.h2("Sidebar")
    ui.input_selectize(
        "selected_attribute",
        "Select Attribute",
        ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
    )
    ui.input_checkbox_group(
        "selected_species_list",
        "Select Species",
        ["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie"],
        inline=True,
    )
    ui.input_numeric("plotly_bin_count", "Plotly Bin Count", 30)
    ui.input_slider(
        "seaborn_bin_count",
        "Seaborn Bin Count",
        1,
        100,
        20,
    )
    ui.hr()
    ui.a(
        "GitHub",
        href="https://github.com/kcbreum/cintel-02-data-kcbreum",
        target="_blank",
    )

# Display data table

with ui.accordion(id="acc", open="closed"):
    with ui.accordion_panel("Data Table"):
        @render.data_frame
        def penguin_datatable():
            return render.DataTable(filtered_data())

# Display data grid
    with ui.accordion_panel("Data Grid"):
        @render.data_frame
        def penguin_datagrid():
            return render.DataGrid(filtered_data())

# Display Plotly histogram
with ui.navset_card_tab(id="tab"):
    with ui.nav_panel("Plotly Histogram"):

        @render_plotly
        def plotly_histogram():
            plotly_hist = px.histogram(
                data_frame=filtered_data(),
                x=input.selected_attribute(),
                nbins=input.plotly_bin_count(),
                color="species",
            ).update_layout(
                title="Plotly Penguins Data",
                xaxis_title="Selected Attribute",
                yaxis_title="Count",
            )
            return plotly_hist

# Display Seaborn histogram    
    with ui.nav_panel("Seaborn Histogram"):
        @render.plot
        def seaborn_histogram():
            histplot = sns.histplot(data=filtered_data(), x="body_mass_g", bins=input.seaborn_bin_count())
            histplot.set_title("Palmer Penguins")
            histplot.set_xlabel("Mass")
            histplot.set_ylabel("Count")
            return histplot

# Display Plotly Scatterplot
with ui.card(full_screen=True):
    ui.card_header("Plotly Scatterplot: Species")

    @render_plotly
    def plotly_scatterplot():
        return px.scatter(filtered_data(),
            title="Penguin Species",
            x="flipper_length_mm",
            y="body_mass_g",
            color="species",
            size_max=8,
            labels={"flipper_length_mm": "Flipper Length (mm)", "body_mass_g": "Body Mass (g)"})

# Reactive calculations and effects
@reactive.calc
@reactive.calc
def filtered_data():
    selected_attribute = input.selected_attribute()
    selected_species_list = input.selected_species_list()
    isSpeciesMatch = penguins_df["species"].isin(selected_species_list)
    filtered_df = penguins_df[isSpeciesMatch]
    return filtered_df
