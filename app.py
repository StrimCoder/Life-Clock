import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Initialize the Dash app with external stylesheets
app = dash.Dash(__name__, 
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
server = app.server

# Define colors
colors = {
    'background': '#f8f9fa',
    'text': '#343a40',
    'primary': '#007bff',
    'secondary': '#6c757d',
    'success': '#28a745',
    'card': '#ffffff',
    'sleep': '#8e44ad',
    'work': '#3498db',
    'phone': '#e74c3c',
    'exercise': '#2ecc71',
    'others': '#f39c12'
}

app.layout = html.Div(style={
    'fontFamily': 'Roboto, Arial, sans-serif',
    'backgroundColor': colors['background'],
    'minHeight': '100vh',
    'padding': '20px'
}, children=[
    # Header
    html.Div(style={
        'backgroundColor': colors['card'],
        'borderRadius': '10px',
        'padding': '20px',
        'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)',
        'marginBottom': '20px'
    }, children=[
        html.H1("🕰️ Life Clock Dashboard", style={
            'textAlign': 'center',
            'color': colors['primary'],
            'marginBottom': '10px'
        }),
        html.P("Visualize how you spend your time throughout your life", style={
            'textAlign': 'center',
            'color': colors['secondary'],
            'fontSize': '18px'
        })
    ]),
    
    # Input Section
    html.Div(style={
        'backgroundColor': colors['card'],
        'borderRadius': '10px',
        'padding': '20px',
        'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)',
        'marginBottom': '20px'
    }, children=[
        # Age Input
        html.Div(style={'marginBottom': '20px'}, children=[
            html.Label("How old are you?", style={
                'fontWeight': 'bold',
                'fontSize': '16px',
                'color': colors['text'],
                'marginBottom': '10px',
                'display': 'block'
            }),
            dcc.Input(
                id='age-input',
                type='number',
                min=1,
                max=100,
                value=25,
                style={
                    'width': '100%',
                    'padding': '8px',
                    'borderRadius': '5px',
                    'border': f'1px solid {colors["secondary"]}',
                    'fontSize': '16px'
                }
            ),
        ]),
        
        # Activity Inputs
        html.Div(style={'marginBottom': '20px'}, children=[
            html.Label("Daily Activities (hours)", style={
                'fontWeight': 'bold',
                'fontSize': '16px',
                'color': colors['text'],
                'marginBottom': '15px',
                'display': 'block'
            }),
            
            # Activity inputs grid
            html.Div(style={
                'display': 'grid',
                'gridTemplateColumns': 'repeat(auto-fill, minmax(200px, 1fr))',
                'gap': '15px'
            }, children=[
                # Sleep
                html.Div(children=[
                    html.Label("Sleep", style={
                        'color': colors['sleep'],
                        'display': 'block',
                        'marginBottom': '5px'
                    }),
                    dcc.Input(
                        id='sleep-input',
                        type='number',
                        min=0,
                        max=24,
                        step=0.5,
                        value=7,
                        style={
                            'width': '100%',
                            'padding': '8px',
                            'borderRadius': '5px',
                            'border': f'1px solid {colors["sleep"]}',
                            'fontSize': '16px'
                        }
                    ),
                ]),
                
                # Work
                html.Div(children=[
                    html.Label("Work", style={
                        'color': colors['work'],
                        'display': 'block',
                        'marginBottom': '5px'
                    }),
                    dcc.Input(
                        id='work-input',
                        type='number',
                        min=0,
                        max=24,
                        step=0.5,
                        value=8,
                        style={
                            'width': '100%',
                            'padding': '8px',
                            'borderRadius': '5px',
                            'border': f'1px solid {colors["work"]}',
                            'fontSize': '16px'
                        }
                    ),
                ]),
                
                # Phone
                html.Div(children=[
                    html.Label("Phone", style={
                        'color': colors['phone'],
                        'display': 'block',
                        'marginBottom': '5px'
                    }),
                    dcc.Input(
                        id='phone-input',
                        type='number',
                        min=0,
                        max=24,
                        step=0.5,
                        value=3,
                        style={
                            'width': '100%',
                            'padding': '8px',
                            'borderRadius': '5px',
                            'border': f'1px solid {colors["phone"]}',
                            'fontSize': '16px'
                        }
                    ),
                ]),
                
                # Exercise
                html.Div(children=[
                    html.Label("Exercise", style={
                        'color': colors['exercise'],
                        'display': 'block',
                        'marginBottom': '5px'
                    }),
                    dcc.Input(
                        id='exercise-input',
                        type='number',
                        min=0,
                        max=24,
                        step=0.5,
                        value=1,
                        style={
                            'width': '100%',
                            'padding': '8px',
                            'borderRadius': '5px',
                            'border': f'1px solid {colors["exercise"]}',
                            'fontSize': '16px'
                        }
                    ),
                ]),
                
                # Others
                html.Div(children=[
                    html.Label("Others", style={
                        'color': colors['others'],
                        'display': 'block',
                        'marginBottom': '5px'
                    }),
                    dcc.Input(
                        id='others-input',
                        type='number',
                        min=0,
                        max=24,
                        step=0.5,
                        value=5,
                        style={
                            'width': '100%',
                            'padding': '8px',
                            'borderRadius': '5px',
                            'border': f'1px solid {colors["others"]}',
                            'fontSize': '16px'
                        }
                    ),
                ]),
            ]),
        ]),
        
        # Total Hours Display
        html.Div(id='total-hours-display', style={
            'textAlign': 'center',
            'fontSize': '18px',
            'fontWeight': 'bold',
            'marginBottom': '20px',
            'padding': '10px',
            'backgroundColor': colors['background'],
            'borderRadius': '5px'
        }),
        
        # Update Button
        html.Button('Update Dashboard', 
                   id='submit-button', 
                   n_clicks=0,
                   style={
                       'backgroundColor': colors['primary'],
                       'color': 'white',
                       'border': 'none',
                       'padding': '10px 20px',
                       'borderRadius': '5px',
                       'fontSize': '16px',
                       'cursor': 'pointer',
                       'width': '100%'
                   })
    ]),
    
    # Results Container
    html.Div(id='output-container', style={'marginTop': '20px'})
])

# Callback for updating total hours display
@app.callback(
    Output('total-hours-display', 'children'),
    [Input('sleep-input', 'value'),
     Input('work-input', 'value'),
     Input('phone-input', 'value'),
     Input('exercise-input', 'value'),
     Input('others-input', 'value')]
)
def update_total_hours(sleep, work, phone, exercise, others):
    # Handle None values that might occur when inputs are cleared
    values = [v if v is not None else 0 for v in [sleep, work, phone, exercise, others]]
    sleep, work, phone, exercise, others = values
    
    total = sleep + work + phone + exercise + others
    
    if total > 24:
        return html.Div([
            html.Span("⚠️ Total: ", style={'color': '#dc3545'}),
            html.Span(f"{total} hours ", style={'color': '#dc3545', 'fontWeight': 'bold'}),
            html.Span("(exceeds 24 hours)", style={'color': '#dc3545'})
        ])
    else:
        return html.Div([
            html.Span("Total: ", style={'color': colors['text']}),
            html.Span(f"{total} hours", style={'color': colors['primary'], 'fontWeight': 'bold'})
        ])

# Main dashboard callback
@app.callback(
    Output('output-container', 'children'),
    Input('submit-button', 'n_clicks'),
    State('age-input', 'value'),
    State('sleep-input', 'value'),
    State('work-input', 'value'),
    State('phone-input', 'value'),
    State('exercise-input', 'value'),
    State('others-input', 'value')
)
def update_dashboard(n_clicks, age, sleep, work, phone, exercise, others):
    if n_clicks == 0:
        return ""
    
    total_hours = sleep + work + phone + exercise + others
    if total_hours > 24:
        return html.Div([
            html.Div("❌ Total hours exceed 24! Please adjust your inputs.", 
                    style={
                        'color': 'white',
                        'backgroundColor': '#dc3545',
                        'padding': '15px',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'marginBottom': '20px'
                    })
        ])
    
    lifespan_years = 80
    days_lived = age * 365
    days_remaining = (lifespan_years - age) * 365
    
    activity_hours_per_day = [sleep, work, phone, exercise, others]
    activities = ['Sleep', 'Work', 'Phone', 'Exercise', 'Others']
    colors_list = [colors['sleep'], colors['work'], colors['phone'], colors['exercise'], colors['others']]
    
    time_spent = [(h * days_lived) / 24 for h in activity_hours_per_day]
    time_left = [(h * days_remaining) / 24 for h in activity_hours_per_day]
    
    # Create pie chart
    fig_pie = px.pie(
        names=activities, 
        values=activity_hours_per_day, 
        title="Daily Time Distribution",
        color_discrete_sequence=colors_list
    )
    fig_pie.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['card'],
        font={'color': colors['text']},
        legend={'orientation': 'h', 'y': -0.1}
    )
    
    # Create bar chart
    fig_bar = go.Figure()
    fig_bar.add_trace(go.Bar(
        name='Days Spent',
        x=activities,
        y=time_spent,
        marker_color=colors_list
    ))
    fig_bar.add_trace(go.Bar(
        name='Days Remaining',
        x=activities,
        y=time_left,
        marker_color=[f"rgba({int(int(c[1:3], 16))}, {int(int(c[3:5], 16))}, {int(int(c[5:7], 16))}, 0.5)" for c in colors_list]
    ))
    fig_bar.update_layout(
        barmode='group',
        title="Lifetime Days per Activity",
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['card'],
        font={'color': colors['text']},
        legend={'orientation': 'h', 'y': -0.1}
    )
    
    # Create gauge chart
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=age,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Life Progress", 'font': {'color': colors['text']}},
        delta={'reference': lifespan_years/2, 'increasing': {'color': colors['secondary']}},
        gauge={
            'axis': {'range': [0, lifespan_years], 'tickcolor': colors['text']},
            'bar': {'color': colors['primary']},
            'bgcolor': colors['background'],
            'bordercolor': colors['text'],
            'steps': [
                {'range': [0, lifespan_years*0.25], 'color': "rgba(46, 204, 113, 0.3)"},
                {'range': [lifespan_years*0.25, lifespan_years*0.5], 'color': "rgba(241, 196, 15, 0.3)"},
                {'range': [lifespan_years*0.5, lifespan_years*0.75], 'color': "rgba(230, 126, 34, 0.3)"},
                {'range': [lifespan_years*0.75, lifespan_years], 'color': "rgba(231, 76, 60, 0.3)"}
            ]
        }
    ))
    fig_gauge.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['card'],
        height=300
    )
    
    # Summary statistics
    years_left = lifespan_years - age
    days_left = years_left * 365
    
    # Create dashboard layout
    return html.Div([
        # Summary cards
        html.Div(style={
            'display': 'flex',
            'flexWrap': 'wrap',
            'gap': '20px',
            'marginBottom': '20px'
        }, children=[
            # Age card
            html.Div(style={
                'flex': '1',
                'backgroundColor': colors['card'],
                'padding': '20px',
                'borderRadius': '10px',
                'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)',
                'textAlign': 'center'
            }, children=[
                html.H3(f"Age: {age}", style={'color': colors['primary']}),
                html.P(f"You have approximately {years_left} years or {days_left:,} days left")
            ]),
            
            # Hours card
            html.Div(style={
                'flex': '1',
                'backgroundColor': colors['card'],
                'padding': '20px',
                'borderRadius': '10px',
                'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)',
                'textAlign': 'center'
            }, children=[
                html.H3(f"Daily Hours: {total_hours}", style={'color': colors['primary']}),
                html.P(f"You have {24-total_hours} hours of unallocated time each day")
            ])
        ]),
        
        # Charts
        html.Div(style={
            'display': 'flex',
            'flexWrap': 'wrap',
            'gap': '20px',
            'marginBottom': '20px'
        }, children=[
            # Gauge chart
            html.Div(style={
                'flex': '1',
                'minWidth': '300px',
                'backgroundColor': colors['card'],
                'padding': '20px',
                'borderRadius': '10px',
                'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)'
            }, children=[
                dcc.Graph(figure=fig_gauge, config={'displayModeBar': False})
            ]),
            
            # Pie chart
            html.Div(style={
                'flex': '1',
                'minWidth': '300px',
                'backgroundColor': colors['card'],
                'padding': '20px',
                'borderRadius': '10px',
                'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)'
            }, children=[
                dcc.Graph(figure=fig_pie)
            ])
        ]),
        
        # Bar chart (full width)
        html.Div(style={
            'backgroundColor': colors['card'],
            'padding': '20px',
            'borderRadius': '10px',
            'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)'
        }, children=[
            dcc.Graph(figure=fig_bar)
        ])
    ])

if __name__ == '__main__':
    app.run(debug=True)
