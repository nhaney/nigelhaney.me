import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import PropTypes from 'prop-types';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';

import dateConverter from '../../utils/utils'
import '../../styles/blog_preview.css'

class BlogPreviewItem extends Component {
	constructor(props) {
		super(props);

		this.state = {
			item:this.props.item
		};
	}
	render() {
		let published_date = dateConverter(this.state.item.published_time)
		return (
					<Link to={{
								pathname: this.state.item.unique_url,
								state: {
									item: this.state.item
								}
							}} 
								style={{color:"black", textDecoration:"none"}}>
						<Card className="previewItem">
							<Card.Body>
								<Card.Title>{this.state.item.post_title}</Card.Title>
								<Card.Text>{this.state.item.excerpt}</Card.Text>
								<Button variant="primary">
									View
								</Button>
							</Card.Body>
							<Card.Footer className="text-muted">
							Published: {published_date}
							<br />
							Comments: {this.state.item.comment_count}
							</Card.Footer>
						</Card>
					</Link>
		);
	}
}

BlogPreviewItem.propTypes = {
	item: PropTypes.object.isRequired
}

export default BlogPreviewItem;
