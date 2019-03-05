import React, { Component } from 'react';
import axios from 'axios';

import BlogPreviewItem from './BlogPreviewItem';

import '../../styles/blog_preview.css'

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Loader from 'react-loader-spinner';


class BlogPreview extends Component {

	constructor(props) {
		super(props);

		this.state = {
			posts: [],
			isLoading: true,
			hasErrored: false,
			errorMessage: ""
		};
	}

	componentDidMount(){
		axios.get("https://nigelhaney.me/api/blog/posts")
					.then(res => {
						// console.log(res);
						this.setState({posts: res.data.data, isLoading:false});
					})
					.catch(error => {
						// console.log(error)
						this.setState({hasErrored:true, isLoading:false, errorMessage:error.response.data.message})
					});
	}

	render() {
		return(
			<Container style={{paddingLeft:"0px", paddingRight: "0px"}} className="d-flex flex-row flex-wrap align-items-start justify-content-center">
				{this.state.isLoading &&
					<Container>
						<Row className="justify-content-md-center">
							<h3>Loading blog posts...</h3>
						</Row>
						<Row className="justify-content-md-center">
							<Loader type="TailSpin" color="#000" height="75" width="75"/>
						</Row>
					</Container>
				}
				{!this.state.isLoading && this.state.hasErrored &&
					<Container>
						<Row className="justify-content-md-center">
							<h3 style={{color:"red"}}>Error loading posts.</h3>
						</Row>
						<Row className="justify-content-md-center">
							<h4>{this.state.errorMessage}</h4>
						</Row>
					</Container>
				}
				{
					!this.state.isLoading &&
					this.state.posts.map((item) => {
						return(
								<BlogPreviewItem key={item.post_id} item={item} />
						)
					})
				}
			</Container>
		)
	}
}

export default BlogPreview;
