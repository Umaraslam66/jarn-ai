import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import time

# Page configuration
st.set_page_config(
    page_title="RailwayAI Copilot",
    page_icon="🚄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    .metric-card {
        background: #f8fafc;
        padding: 1.5rem;
        border-radius: 0.75rem;
        border: 1px solid #e2e8f0;
        margin-bottom: 1rem;
    }
    .stButton>button {
        background: linear-gradient(90deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        border: none;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        border-radius: 0.5rem;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(37, 99, 235, 0.4);
    }
    .ai-response {
        background: #f0f9ff;
        border-left: 4px solid #3b82f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .warning-box {
        background: #fef3c7;
        border-left: 4px solid #f59e0b;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'current_view' not in st.session_state:
    st.session_state.current_view = "Dashboard"

# Sidebar navigation
with st.sidebar:
    st.markdown("## 🚄 RailwayAI Copilot")
    st.markdown("AI-Powered Railway Planning Assistant")
    
    st.markdown("---")
    
    # Navigation menu
    menu_items = {
        "Dashboard": "📊",
        "AI Assistant": "🤖",
        "Timetable Manager": "📅",
        "Network Visualization": "🗺️",
        "Document Intelligence": "📚",
        "Simulation & Optimization": "⚡",
        "Analytics & Reports": "📈",
        "Settings": "⚙️"
    }
    
    for item, icon in menu_items.items():
        if st.button(f"{icon} {item}", key=item, use_container_width=True):
            st.session_state.current_view = item
    
    st.markdown("---")
    
    # Quick stats
    st.markdown("### System Status")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("AI Model", "GPT-4", "Active")
    with col2:
        st.metric("Data Sync", "Live", "✓")
    
    st.markdown("### Quick Actions")
    if st.button("🔄 Sync Timetables", use_container_width=True):
        st.success("Timetables synchronized!")
    if st.button("📥 Import Network Data", use_container_width=True):
        st.info("Network data import started...")

# Main content area
if st.session_state.current_view == "Dashboard":
    st.markdown('<h1 class="main-header">Railway Operations Dashboard</h1>', unsafe_allow_html=True)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Active Trains",
            value="127",
            delta="12 from yesterday",
            delta_color="normal"
        )
    
    with col2:
        st.metric(
            label="On-Time Performance",
            value="94.3%",
            delta="2.1%",
            delta_color="normal"
        )
    
    with col3:
        st.metric(
            label="Network Utilization",
            value="78.5%",
            delta="-3.2%",
            delta_color="inverse"
        )
    
    with col4:
        st.metric(
            label="Active Disruptions",
            value="3",
            delta="-2",
            delta_color="inverse"
        )
    
    # Real-time train movements chart
    st.markdown("### Real-Time Train Movements")
    
    # Generate dummy data for train movements
    hours = pd.date_range(start='2024-01-01', periods=24, freq='H')
    train_data = pd.DataFrame({
        'Hour': hours,
        'Northbound': np.random.randint(10, 30, 24),
        'Southbound': np.random.randint(10, 30, 24),
        'Eastbound': np.random.randint(5, 20, 24),
        'Westbound': np.random.randint(5, 20, 24)
    })
    
    fig = go.Figure()
    for direction in ['Northbound', 'Southbound', 'Eastbound', 'Westbound']:
        fig.add_trace(go.Scatter(
            x=train_data['Hour'],
            y=train_data[direction],
            mode='lines+markers',
            name=direction,
            line=dict(width=3)
        ))
    
    fig.update_layout(
        title="Train Movements by Direction",
        xaxis_title="Time",
        yaxis_title="Number of Trains",
        hovermode='x unified',
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Current issues and AI recommendations
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### ⚠️ Current Issues")
        issues = [
            {"type": "Delay", "location": "Central Station", "impact": "High", "trains": 5},
            {"type": "Maintenance", "location": "Track 3-4", "impact": "Medium", "trains": 2},
            {"type": "Weather", "location": "Northern Line", "impact": "Low", "trains": 1}
        ]
        
        for issue in issues:
            if issue["impact"] == "High":
                st.error(f"**{issue['type']}** at {issue['location']} - Affecting {issue['trains']} trains")
            elif issue["impact"] == "Medium":
                st.warning(f"**{issue['type']}** at {issue['location']} - Affecting {issue['trains']} trains")
            else:
                st.info(f"**{issue['type']}** at {issue['location']} - Affecting {issue['trains']} trains")
    
    with col2:
        st.markdown("### 🤖 AI Recommendations")
        st.markdown('<div class="ai-response">', unsafe_allow_html=True)
        st.markdown("""
        **Optimization Opportunities Detected:**
        
        1. **Reroute Train 547** via Track 2 to avoid Central Station congestion
        2. **Adjust Schedule** for Northern Line - 5 min intervals recommended
        3. **Preventive Maintenance** suggested for Track 7-8 based on usage patterns
        """)
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_view == "AI Assistant":
    st.markdown('<h1 class="main-header">AI Railway Planning Assistant</h1>', unsafe_allow_html=True)
    
    # Example prompts
    st.markdown("### Quick Prompts")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🚂 Optimize morning schedule", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": "Optimize the morning schedule for maximum efficiency"})
    
    with col2:
        if st.button("📊 Analyze last week's delays", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": "Analyze all delays from last week and identify patterns"})
    
    with col3:
        if st.button("🔧 Maintenance planning", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": "Create optimal maintenance schedule for next month"})
    
    # Chat interface
    st.markdown("### Chat with AI Assistant")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask anything about railway operations..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.write(prompt)
        
        # Simulate AI response
        with st.chat_message("assistant"):
            with st.spinner("Analyzing railway data..."):
                time.sleep(1)
            
            # Generate contextual response based on keywords
            if "optimize" in prompt.lower() or "schedule" in prompt.lower():
                response = """Based on my analysis of current railway operations:

**Schedule Optimization Recommendations:**

1. **Peak Hours Adjustment**: Increase frequency on Lines 1, 3, and 5 between 7:00-9:00 AM
2. **Platform Utilization**: Platform 4 is underutilized - suggest rerouting 3 services
3. **Connection Optimization**: Reduce transfer time at Central Hub by 2 minutes

**Expected Impact:**
- 15% reduction in average passenger wait time
- 8% increase in network capacity
- €45,000 monthly operational savings

Would you like me to generate a detailed implementation plan?"""
            
            elif "delay" in prompt.lower() or "analyze" in prompt.lower():
                response = """**Delay Analysis Results:**

📊 **Key Findings:**
- 73% of delays occur during morning rush (6:00-9:00 AM)
- Primary cause: Signal failures at junction points (42%)
- Secondary cause: Platform congestion (31%)

📈 **Trending Patterns:**
- Tuesday and Thursday show 23% more delays
- Weather-related delays increased by 15% this month

💡 **Recommended Actions:**
1. Upgrade signaling system at Junction A and C
2. Implement dynamic platform assignment
3. Add buffer time for weather-sensitive routes

Shall I create a detailed report with visualizations?"""
            
            else:
                response = """I understand your query. Let me analyze the relevant railway data for you.

Based on our comprehensive database of:
- National timetables
- Network topology
- Historical performance data
- Regulatory requirements

I can help you with:
✓ Schedule optimization
✓ Capacity planning
✓ Delay analysis and predictions
✓ Maintenance scheduling
✓ Regulatory compliance checks
✓ Route planning and optimization

Please provide more specific details about what you'd like to analyze or optimize."""
            
            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

elif st.session_state.current_view == "Timetable Manager":
    st.markdown('<h1 class="main-header">Intelligent Timetable Management</h1>', unsafe_allow_html=True)
    
    # Timetable controls
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        selected_line = st.selectbox("Select Railway Line", ["All Lines", "Line 1 - Express", "Line 2 - Regional", "Line 3 - Freight", "Line 4 - High Speed"])
    
    with col2:
        selected_date = st.date_input("Date", datetime.now())
    
    with col3:
        view_mode = st.radio("View Mode", ["Schedule", "Gantt Chart"])
    
    if view_mode == "Schedule":
        # Generate dummy timetable data
        timetable_data = []
        stations = ["Central Station", "North Terminal", "East Junction", "South Plaza", "West End"]
        
        for i in range(20):
            train_id = f"TR{1000 + i}"
            start_time = datetime.now().replace(hour=5, minute=0) + timedelta(minutes=i*15)
            
            for j, station in enumerate(stations):
                arrival = start_time + timedelta(minutes=j*12)
                departure = arrival + timedelta(minutes=2)
                
                timetable_data.append({
                    "Train ID": train_id,
                    "Station": station,
                    "Arrival": arrival.strftime("%H:%M"),
                    "Departure": departure.strftime("%H:%M"),
                    "Platform": np.random.randint(1, 6),
                    "Status": np.random.choice(["On Time", "On Time", "On Time", "Delayed", "Early"])
                })
        
        df_timetable = pd.DataFrame(timetable_data)
        
        # Add status coloring
        def color_status(val):
            if val == "Delayed":
                return 'background-color: #fee2e2'
            elif val == "Early":
                return 'background-color: #dbeafe'
            else:
                return 'background-color: #d1fae5'
        
        styled_df = df_timetable.style.applymap(color_status, subset=['Status'])
        st.dataframe(styled_df, use_container_width=True, height=400)
        
    else:  # Gantt Chart view
        st.markdown("### Train Schedule Visualization")
        
        # Create Gantt chart data
        gantt_data = []
        trains = [f"Train {i}" for i in range(101, 111)]
        
        for i, train in enumerate(trains):
            start = datetime.now().replace(hour=6, minute=0) + timedelta(minutes=i*20)
            end = start + timedelta(hours=np.random.randint(2, 6))
            
            gantt_data.append({
                "Train": train,
                "Start": start,
                "End": end,
                "Line": f"Line {(i % 4) + 1}"
            })
        
        df_gantt = pd.DataFrame(gantt_data)
        
        fig = px.timeline(df_gantt, x_start="Start", x_end="End", y="Train", color="Line",
                         title="Train Schedule Timeline")
        fig.update_yaxes(autorange="reversed")
        st.plotly_chart(fig, use_container_width=True)
    
    # AI optimization panel
    st.markdown("### 🤖 AI Timetable Optimization")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        optimization_goal = st.selectbox(
            "Optimization Goal",
            ["Minimize Delays", "Maximize Throughput", "Energy Efficiency", "Passenger Comfort"]
        )
    
    with col2:
        if st.button("Run AI Optimization", type="primary"):
            with st.spinner("Running advanced optimization algorithms..."):
                time.sleep(2)
            st.success("Optimization complete! 12% improvement in selected metric achieved.")
            st.markdown('<div class="ai-response">New optimized timetable ready for review. Key improvements: Reduced platform conflicts by 23%, improved connection times by 15%.</div>', unsafe_allow_html=True)

elif st.session_state.current_view == "Network Visualization":
    st.markdown('<h1 class="main-header">Railway Network Visualization</h1>', unsafe_allow_html=True)
    
    # Network view controls
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        view_type = st.selectbox("View Type", ["Geographic", "Schematic", "3D View"])
    
    with col2:
        show_trains = st.checkbox("Show Live Trains", value=True)
    
    with col3:
        show_disruptions = st.checkbox("Show Disruptions", value=True)
    
    with col4:
        if st.button("🔄 Refresh", type="primary"):
            st.success("Network data refreshed!")
    
    # Create network visualization
    st.markdown("### Railway Network Map")
    
    # Generate dummy network data
    stations_data = pd.DataFrame({
        'station': ['Central', 'North', 'South', 'East', 'West', 'Junction A', 'Junction B'],
        'lat': [40.7128, 40.7580, 40.6892, 40.7489, 40.6892, 40.7300, 40.7000],
        'lon': [-74.0060, -73.9855, -74.0445, -73.9680, -73.9900, -73.9950, -74.0200],
        'size': [30, 20, 20, 20, 20, 15, 15],
        'type': ['Major Hub', 'Terminal', 'Terminal', 'Terminal', 'Terminal', 'Junction', 'Junction']
    })
    
    fig = go.Figure()
    
    # Add station markers
    for station_type in stations_data['type'].unique():
        df_filtered = stations_data[stations_data['type'] == station_type]
        fig.add_trace(go.Scattermapbox(
            lat=df_filtered['lat'],
            lon=df_filtered['lon'],
            mode='markers',
            marker=dict(size=df_filtered['size']),
            text=df_filtered['station'],
            name=station_type
        ))
    
    # Add railway lines
    lines = [
        {'start': [40.7128, -74.0060], 'end': [40.7580, -73.9855]},
        {'start': [40.7128, -74.0060], 'end': [40.6892, -74.0445]},
        {'start': [40.7128, -74.0060], 'end': [40.7489, -73.9680]},
        {'start': [40.7128, -74.0060], 'end': [40.6892, -73.9900]}
    ]
    
    for line in lines:
        fig.add_trace(go.Scattermapbox(
            lat=[line['start'][0], line['end'][0]],
            lon=[line['start'][1], line['end'][1]],
            mode='lines',
            line=dict(width=3, color='blue'),
            showlegend=False
        ))
    
    fig.update_layout(
        mapbox=dict(
            style="open-street-map",
            zoom=10,
            center=dict(lat=40.7128, lon=-74.0060)
        ),
        height=600,
        margin=dict(t=0, b=0, l=0, r=0)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Network statistics
    st.markdown("### Network Statistics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Track Length", "2,847 km")
        st.metric("Stations", "147")
    
    with col2:
        st.metric("Daily Passengers", "1.2M")
        st.metric("Active Signals", "3,421")
    
    with col3:
        st.metric("Network Health", "96.7%")
        st.metric("Maintenance Due", "12 sections")

elif st.session_state.current_view == "Document Intelligence":
    st.markdown('<h1 class="main-header">Document Intelligence & RAG System</h1>', unsafe_allow_html=True)
    
    # Document search interface
    st.markdown("### 🔍 Intelligent Document Search")
    
    search_query = st.text_input("Search regulations, standards, and operational documents", placeholder="e.g., safety protocols for level crossings")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        doc_type = st.multiselect("Document Type", ["Regulations", "Standards", "Procedures", "Manuals", "Reports"])
    with col2:
        date_range = st.select_slider("Date Range", ["Last Week", "Last Month", "Last Year", "All Time"])
    with col3:
        relevance = st.slider("Relevance Threshold", 0.0, 1.0, 0.7)
    
    if st.button("Search Documents", type="primary") or search_query:
        with st.spinner("Searching through knowledge base..."):
            time.sleep(1)
        
        # Dummy search results
        results = [
            {
                "title": "Railway Safety Regulations 2024 - Section 5.3",
                "relevance": 0.95,
                "excerpt": "Level crossing safety protocols require automated barrier systems with redundant sensors...",
                "doc_type": "Regulation",
                "date": "2024-03-15"
            },
            {
                "title": "Operational Manual - Track Maintenance Standards",
                "relevance": 0.87,
                "excerpt": "Regular inspection intervals for level crossings must not exceed 30 days...",
                "doc_type": "Manual",
                "date": "2024-01-10"
            },
            {
                "title": "EU Directive 2023/847 - Railway Interoperability",
                "relevance": 0.82,
                "excerpt": "Cross-border operations require compliance with unified safety standards...",
                "doc_type": "Standard",
                "date": "2023-11-20"
            }
        ]
        
        st.markdown("### Search Results")
        for result in results:
            with st.expander(f"{result['title']} (Relevance: {result['relevance']:.0%})"):
                st.markdown(f"**Type:** {result['doc_type']} | **Date:** {result['date']}")
                st.markdown(f"_{result['excerpt']}_")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.button("View Full Document", key=f"view_{result['title']}")
                with col2:
                    st.button("Add to Workspace", key=f"add_{result['title']}")
                with col3:
                    st.button("Generate Summary", key=f"summary_{result['title']}")
    
    # Knowledge base stats
    st.markdown("### 📚 Knowledge Base Statistics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Documents", "12,847", "234 added this month")
    with col2:
        st.metric("Regulations", "3,421", "12 updated")
    with col3:
        st.metric("Standards", "1,893", "5 new")
    with col4:
        st.metric("Last Sync", "2 hours ago", "✓")

elif st.session_state.current_view == "Simulation & Optimization":
    st.markdown('<h1 class="main-header">Simulation & Optimization Engine</h1>', unsafe_allow_html=True)
    
    # Simulation controls
    st.markdown("### 🎮 Simulation Parameters")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        simulation_type = st.selectbox(
            "Simulation Type",
            ["Traffic Flow", "Disruption Recovery", "Capacity Planning", "Energy Optimization"]
        )
    
    with col2:
        time_horizon = st.selectbox(
            "Time Horizon",
            ["1 Hour", "6 Hours", "1 Day", "1 Week", "1 Month"]
        )
    
    with col3:
        confidence_level = st.slider("Confidence Level", 80, 99, 95)
    
    # Advanced settings
    with st.expander("Advanced Settings"):
        col1, col2 = st.columns(2)
        with col1:
            st.number_input("Monte Carlo Iterations", 100, 10000, 1000)
            st.selectbox("Algorithm", ["Genetic Algorithm", "Simulated Annealing", "Particle Swarm"])
        with col2:
            st.number_input("Random Seed", 0, 9999, 42)
            st.checkbox("Include Weather Patterns", value=True)
    
    # Run simulation button
    if st.button("🚀 Run Simulation", type="primary", use_container_width=True):
        # Progress bar
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(100):
            progress_bar.progress(i + 1)
            status_text.text(f"Running simulation... {i+1}%")
            time.sleep(0.02)
        
        status_text.text("Simulation complete!")
        
        # Results
        st.markdown("### 📊 Simulation Results")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Generate simulation result chart
            x = np.linspace(0, 24, 100)
            baseline = 75 + 10 * np.sin(x/4)
            optimized = 85 + 8 * np.sin(x/4)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x, y=baseline, name='Baseline', line=dict(color='red', width=2)))
            fig.add_trace(go.Scatter(x=x, y=optimized, name='Optimized', line=dict(color='green', width=2)))
            fig.update_layout(
                title="Network Performance Comparison",
                xaxis_title="Time (hours)",
                yaxis_title="Performance Score",
                hovermode='x unified'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("### Key Findings")
            st.metric("Performance Gain", "+13.7%", "vs baseline")
            st.metric("Cost Savings", "€127,500", "per month")
            st.metric("CO₂ Reduction", "-8.2%", "emissions")
            
            st.markdown("### Recommendations")
            st.info("1. Implement dynamic speed adjustments")
            st.info("2. Optimize platform assignments")
            st.info("3. Adjust maintenance windows")
    
    # Optimization scenarios
    st.markdown("### 💡 Pre-configured Scenarios")
    
    scenarios = [
        {"name": "Rush Hour Optimization", "desc": "Maximize throughput during peak hours", "icon": "🏃"},
        {"name": "Energy Efficiency", "desc": "Minimize energy consumption", "icon": "🔋"},
        {"name": "Delay Recovery", "desc": "Optimal recovery from major disruptions", "icon": "🔧"},
        {"name": "Weekend Service", "desc": "Balance maintenance and passenger service", "icon": "🏗️"}
    ]
    
    cols = st.columns(2)
    for i, scenario in enumerate(scenarios):
        with cols[i % 2]:
            if st.button(f"{scenario['icon']} {scenario['name']}", key=f"scenario_{i}", use_container_width=True):
                st.info(f"Loading scenario: {scenario['desc']}")

elif st.session_state.current_view == "Analytics & Reports":
    st.markdown('<h1 class="main-header">Analytics & Reporting Dashboard</h1>', unsafe_allow_html=True)
    
    # Report type selection
    report_type = st.selectbox(
        "Select Report Type",
        ["Executive Summary", "Performance Analysis", "Financial Report", "Safety Metrics", "Custom Report"]
    )
    
    # Date range selection
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime.now() - timedelta(days=30))
    with col2:
        end_date = st.date_input("End Date", datetime.now())
    
    # Generate report button
    if st.button("Generate Report", type="primary"):
        with st.spinner("Generating comprehensive report..."):
            time.sleep(2)
        
        st.success("Report generated successfully!")
        
        # Display sample report
        st.markdown(f"## {report_type} - {start_date} to {end_date}")
        
        # KPI Overview
        st.markdown("### Key Performance Indicators")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Overall Performance", "92.3%", "+3.2%")
        with col2:
            st.metric("Revenue", "€4.2M", "+8.5%")
        with col3:
            st.metric("Passenger Satisfaction", "4.3/5", "+0.2")
        with col4:
            st.metric("Safety Score", "98.7%", "+1.1%")
        
        # Charts
        col1, col2 = st.columns(2)
        
        with col1:
            # Performance trend
            dates = pd.date_range(start=start_date, end=end_date, freq='D')
            performance = 85 + np.random.randn(len(dates)) * 5
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=dates, y=performance, mode='lines', name='Performance'))
            fig.update_layout(title="Daily Performance Trend", xaxis_title="Date", yaxis_title="Performance %")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Category breakdown
            categories = ['On-Time', 'Delays < 5min', 'Delays > 5min', 'Cancelled']
            values = [75, 15, 8, 2]
            
            fig = go.Figure(data=[go.Pie(labels=categories, values=values)])
            fig.update_layout(title="Service Performance Breakdown")
            st.plotly_chart(fig, use_container_width=True)
        
        # Export options
        st.markdown("### Export Options")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.button("📄 Export PDF", use_container_width=True)
        with col2:
            st.button("📊 Export Excel", use_container_width=True)
        with col3:
            st.button("📧 Email Report", use_container_width=True)
        with col4:
            st.button("📅 Schedule Reports", use_container_width=True)

elif st.session_state.current_view == "Settings":
    st.markdown('<h1 class="main-header">System Settings</h1>', unsafe_allow_html=True)
    
    # Settings tabs
    tab1, tab2, tab3, tab4 = st.tabs(["General", "AI Configuration", "Data Sources", "User Management"])
    
    with tab1:
        st.markdown("### General Settings")
        st.text_input("Organization Name", value="National Railway Corporation")
        st.selectbox("Language", ["English", "German", "French", "Spanish"])
        st.selectbox("Time Zone", ["UTC", "CET", "EST", "PST"])
        st.selectbox("Units", ["Metric", "Imperial"])
        
        st.markdown("### Notification Preferences")
        st.checkbox("Email Notifications", value=True)
        st.checkbox("SMS Alerts for Critical Events", value=True)
        st.checkbox("Daily Summary Reports", value=True)
    
    with tab2:
        st.markdown("### AI Model Configuration")
        st.selectbox("Primary AI Model", ["GPT-4", "Claude 3", "Custom Fine-tuned Model"])
        st.slider("Response Creativity", 0.0, 1.0, 0.7)
        st.slider("Safety Threshold", 0.0, 1.0, 0.95)
        
        st.markdown("### AI Features")
        st.checkbox("Automatic Schedule Optimization", value=True)
        st.checkbox("Predictive Maintenance Alerts", value=True)
        st.checkbox("Real-time Delay Predictions", value=True)
        st.checkbox("Energy Optimization", value=True)
    
    with tab3:
        st.markdown("### Connected Data Sources")
        
        data_sources = [
            {"name": "National Timetable Database", "status": "Connected", "last_sync": "2 min ago"},
            {"name": "Network Infrastructure DB", "status": "Connected", "last_sync": "5 min ago"},
            {"name": "Weather API", "status": "Connected", "last_sync": "Real-time"},
            {"name": "Maintenance Records", "status": "Connected", "last_sync": "1 hour ago"},
            {"name": "Regulatory Database", "status": "Syncing", "last_sync": "In progress"}
        ]
        
        for source in data_sources:
            col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
            with col1:
                st.text(source["name"])
            with col2:
                if source["status"] == "Connected":
                    st.success(source["status"])
                else:
                    st.warning(source["status"])
            with col3:
                st.text(source["last_sync"])
            with col4:
                st.button("Sync", key=f"sync_{source['name']}")
    
    with tab4:
        st.markdown("### User Management")
        st.text_input("Search Users", placeholder="Enter name or email")
        
        # User table
        users = pd.DataFrame({
            "Name": ["John Smith", "Emma Johnson", "Michael Brown", "Sarah Davis"],
            "Role": ["Admin", "Planner", "Analyst", "Viewer"],
            "Department": ["IT", "Operations", "Analytics", "Management"],
            "Last Active": ["2 min ago", "1 hour ago", "3 hours ago", "1 day ago"]
        })
        
        st.dataframe(users, use_container_width=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.button("➕ Add User", use_container_width=True)
        with col2:
            st.button("✏️ Edit Permissions", use_container_width=True)
        with col3:
            st.button("📊 Usage Report", use_container_width=True)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #6b7280; padding: 1rem;'>
        🚄 RailwayAI Copilot v1.0 | Powered by Advanced AI | © 2024 Your Railway Planning Revolution
    </div>
    """,
    unsafe_allow_html=True
)