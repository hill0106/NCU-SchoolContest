#!/usr/bin/env python3
"""
Test Data Generator for NCU Alumni Employment Analysis

This script generates synthetic test data for testing purposes.
"""

import pandas as pd
import numpy as np
import os
from pathlib import Path

def generate_test_data():
    """Generate synthetic test data for testing"""
    
    # Set random seed for reproducible data
    np.random.seed(42)
    
    # Define college names
    colleges = [
        '工學院', '資訊電機學院', '文學院', '理學院', '管理學院',
        '地球科學學院', '客家學院', '生醫理工學院', '太空及遙測研究中心'
    ]
    
    # Define department names for each college
    departments = {
        '工學院': ['機械工程學系', '土木工程學系', '化學工程與材料工程學系'],
        '資訊電機學院': ['資訊工程學系', '電機工程學系', '通訊工程學系'],
        '文學院': ['中國文學系', '英美語文學系', '法國語文學系'],
        '理學院': ['數學系', '物理學系', '化學學系', '生命科學系'],
        '管理學院': ['企業管理學系', '財務金融學系', '資訊管理學系'],
        '地球科學學院': ['地球科學學系', '大氣科學學系'],
        '客家學院': ['客家語文暨社會科學學系'],
        '生醫理工學院': ['生醫科學與工程學系', '生物醫學工程研究所'],
        '太空及遙測研究中心': ['遙測科技碩士學位學程']
    }
    
    # Define employment status options
    employment_status = [
        '全職工作', '部分工時', '目前非就業中', '家管/料理家務者'
    ]
    
    # Define industry categories
    industries = [
        '專業 、科學及技術服務',
        '出版、影音製作傳播及資通訊服務業',
        '教育業',
        '製造業',
        '金融及保險業',
        '醫療保健及社會工作服務業',
        '營建工程業',
        '運輸及倉儲業',
        '藝術、娛樂及休閒服務業',
        '公共行政及國防、強制性社會安全'
    ]
    
    # Generate data for 1-year post-graduation
    data_1_year = []
    for college in colleges:
        college_departments = departments.get(college, ['未知學系'])
        for dept in college_departments:
            # Generate 20-50 records per department
            n_records = np.random.randint(20, 51)
            for _ in range(n_records):
                data_1_year.append({
                    '第一題': np.random.choice(employment_status, p=[0.7, 0.15, 0.1, 0.05]),
                    '第二題': np.random.choice(industries, p=[0.3, 0.25, 0.15, 0.1, 0.05, 0.05, 0.03, 0.02, 0.02, 0.03]),
                    'leave_school_name': college,
                    'leave_dept_name': dept
                })
    
    # Generate data for 3-year post-graduation
    data_3_year = []
    for college in colleges:
        college_departments = departments.get(college, ['未知學系'])
        for dept in college_departments:
            # Generate 15-40 records per department (fewer than 1-year)
            n_records = np.random.randint(15, 41)
            for _ in range(n_records):
                data_3_year.append({
                    '第一題': np.random.choice(employment_status, p=[0.8, 0.1, 0.05, 0.05]),
                    '第二題': np.random.choice(industries, p=[0.35, 0.2, 0.1, 0.12, 0.08, 0.05, 0.04, 0.03, 0.02, 0.01]),
                    'leave_school_name': college,
                    'leave_dept_name': dept
                })
    
    # Generate data for 5-year post-graduation
    data_5_year = []
    for college in colleges:
        college_departments = departments.get(college, ['未知學系'])
        for dept in college_departments:
            # Generate 10-30 records per department (fewer than 3-year)
            n_records = np.random.randint(10, 31)
            for _ in range(n_records):
                data_5_year.append({
                    '第一題': np.random.choice(employment_status, p=[0.85, 0.08, 0.04, 0.03]),
                    '第四題': np.random.choice(industries, p=[0.4, 0.15, 0.08, 0.15, 0.1, 0.04, 0.03, 0.02, 0.02, 0.01]),
                    'leave_school_name': college,
                    'leave_dept_name': dept
                })
    
    # Create DataFrames
    df_1_year = pd.DataFrame(data_1_year)
    df_3_year = pd.DataFrame(data_3_year)
    df_5_year = pd.DataFrame(data_5_year)
    
    # Create test dataset directory if it doesn't exist
    test_data_dir = Path('test_data')
    test_data_dir.mkdir(exist_ok=True)
    
    # Save test data
    df_1_year.to_csv('test_data/first_test.csv', index=False, encoding='utf-8-sig')
    df_3_year.to_csv('test_data/third_test.csv', index=False, encoding='utf-8-sig')
    df_5_year.to_csv('test_data/fifth_test.csv', index=False, encoding='utf-8-sig')
    
    print("✅ Test data generated successfully!")
    print(f"📊 1-year data: {len(df_1_year)} records")
    print(f"📊 3-year data: {len(df_3_year)} records")
    print(f"📊 5-year data: {len(df_5_year)} records")
    print(f"📁 Test data saved to: {test_data_dir.absolute()}")
    
    return df_1_year, df_3_year, df_5_year

def generate_edge_case_data():
    """Generate edge case test data"""
    
    # Empty data
    empty_df = pd.DataFrame()
    empty_df.to_csv('test_data/empty_test.csv', index=False)
    
    # Data with missing values
    missing_data = pd.DataFrame({
        '第一題': ['全職工作', None, '部分工時', ''],
        '第二題': ['專業 、科學及技術服務', '教育業', None, '製造業'],
        'leave_school_name': ['工學院', '文學院', '理學院', ''],
        'leave_dept_name': ['機械工程學系', None, '數學系', '未知學系']
    })
    missing_data.to_csv('test_data/missing_test.csv', index=False, encoding='utf-8-sig')
    
    # Data with special characters
    special_char_data = pd.DataFrame({
        '第一題': ['全職工作(以接案維生，或個人服務，如幫忙排隊…)', '部分工時*:*', '目前非就業中（請跳答第13題）'],
        '第二題': ['專業 、科學及技術服務', '出版、影音製作傳播及資通訊服務業', '教育業'],
        'leave_school_name': ['工學院', '資訊電機學院', '文學院'],
        'leave_dept_name': ['機械工程學系', '資訊工程學系', '中國文學系']
    })
    special_char_data.to_csv('test_data/special_chars_test.csv', index=False, encoding='utf-8-sig')
    
    print("✅ Edge case test data generated!")

if __name__ == '__main__':
    print("🧪 Generating Test Data for NCU Alumni Employment Analysis")
    print("=" * 60)
    
    # Generate main test data
    df_1, df_3, df_5 = generate_test_data()
    
    # Generate edge case data
    generate_edge_case_data()
    
    print("\n📋 Test Data Summary:")
    print(f"- Normal test data: {len(df_1) + len(df_3) + len(df_5)} total records")
    print("- Edge case data: Empty, missing values, special characters")
    print("- All data saved to test_data/ directory")
    
    print("\n✅ Test data generation complete!")
